import pulp

# Crear el problema de minimización
prob = pulp.LpProblem("Minimizar_Costo_Servidores", pulp.LpMinimize)

# Definir los tipos de servidores, costos y capacidades
servidores = ["Intel_std", "Intel_mejorado", "SGI", "Sun"]
costos = {"Intel_std": 2500, "Intel_mejorado": 5000, "SGI": 9000, "Sun": 18750}
capacidades = {"Intel_std": 30, "Intel_mejorado": 80, "SGI": 200, "Sun": 2000}

# Definir los meses de planeación
meses = [1, 2, 3, 4, 5]

# Definir las variables de decisión (binarias)
x = pulp.LpVariable.dicts("CompraServidor", [(servidor, mes) for servidor in servidores for mes in meses], 0, 1, pulp.LpBinary)

# Definir la demanda de empleados por mes
demanda = {1: 0, 2: 60, 3: 260, 4: 290, 5: 365}

# Función objetivo (minimizar los costos)
prob += pulp.lpSum([costos[servidor] * x[(servidor, mes)] for servidor in servidores for mes in meses]), "Costo_Total"

# Restricciones de capacidad para cubrir la demanda de cada mes
for mes in meses:
    prob += pulp.lpSum([capacidades[servidor] * x[(servidor, m)] for servidor in servidores for m in range(1, mes+1)]) >= demanda[mes], f"DemandaMes{mes}"

# Restricción de presupuesto para los meses 1 y 2
prob += pulp.lpSum([costos[servidor] * x[(servidor, mes)] for servidor in servidores for mes in [1, 2]]) <= 9500, "PresupuestoMes1y2"

# Restricción de servidor potente para manufactura entre los meses 1 y 3
prob += pulp.lpSum([x[(servidor, mes)] for servidor in ["Intel_mejorado", "SGI", "Sun"] for mes in [1, 2, 3]]) >= 1, "ServidorPotenteManufactura"

# Resolver el problema
prob.solve()


# Mostrar los resultados
print("Estado:", pulp.LpStatus[prob.status])
for var in prob.variables():
    print(f"{var.name} = {var.varValue}")

print(f"Costo total: {pulp.value(prob.objective)}")
