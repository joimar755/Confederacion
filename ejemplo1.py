import pulp

# Crear el problema de minimización
Q = pulp.LpProblem("Taller_1_PLAN_DE_PRODUCCIÓN", pulp.LpMinimize)

# Definir las variables de decisión (21 variables)
x = pulp.LpVariable.dicts("x", range(1, 21), cat="Binary")

# Definir las capacidades
capacidades = {
    1: 30, 2: 80, 3: 200, 4: 2000,  # Capacidades para Mes 1
    5: 30, 6: 80, 7: 200, 8: 2000,  # Capacidades para Mes 2
    9: 30, 10: 80, 11: 200, 12: 2000,  # Capacidades para Mes 3
    13: 30, 14: 80, 15: 200, 16: 2000,  # Capacidades para Mes 4
    17: 30, 18: 80, 19: 200, 20: 2000   # Capacidades para Mes 5
}

# Definir la demanda mínima para cada mes
demanda = [0, 60, 260, 290, 365]  # Requerimientos por mes

# Restricciones de capacidad para cubrir la demanda
for mes in range(1, 6):  # Para cada mes
    Q += pulp.lpSum([capacidades[i] * x[i] for i in range((mes-1) * 4 + 1, mes * 4 + 1)]) >= demanda[mes - 1], f"DemandaMes{mes}"

# Restricción de capacidad total (ejemplo)
Q += pulp.lpSum([capacidades[i] * x[i] for i in range(1, 21)]) >= 0, "Restriccion_Capacidad"

# Restricciones adicionales según tu estructura
Q += pulp.lpSum([capacidades[i] * x[i] for i in range(1, 9)]) >= 60, "Restriccion_60"
Q += pulp.lpSum([capacidades[i] * x[i] for i in range(1, 13)]) >= 260, "Restriccion_260"
Q += pulp.lpSum([capacidades[i] * x[i] for i in range(1, 17)]) >= 290, "Restriccion_290"
Q += pulp.lpSum([capacidades[i] * x[i] for i in range(1, 21)]) >= 365, "Restriccion_365"

# Restricción para limitar el número de servidores
Q += pulp.lpSum(x[i] for i in range(1, 10)) <= 1, "RestriccionMaximoServidores"

# Resolver el problema
Q.solve()

# Mostrar los resultados
print("Estado:", pulp.LpStatus[Q.status])
for i in range(1, 21):
    print(f"x{i} = {x[i].varValue}")

print(f"Costo total: {pulp.value(Q.objective)}")
