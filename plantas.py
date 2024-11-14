
import pulp


Q = pulp.LpProblem(
    "SERVIDORES", pulp.LpMinimize
)  # si el problema es de Minimización se debe usar pulp.LpMinimize



x1 = pulp.LpVariable("x1", cat="Binary")
x2 = pulp.LpVariable("x2", cat="Binary")
x3 = pulp.LpVariable("x3", cat="Binary")
x4 = pulp.LpVariable("x4", cat="Binary")
x5 = pulp.LpVariable("x5", cat="Binary")
x6 = pulp.LpVariable("x6", cat="Binary")
x7 = pulp.LpVariable("x7", cat="Binary")
x8 = pulp.LpVariable("x8", cat="Binary")
x9 = pulp.LpVariable("x9", cat="Binary")
x10 = pulp.LpVariable("x10", cat="Binary")
x11 = pulp.LpVariable("x11", cat="Binary")
x12 = pulp.LpVariable("x12", cat="Binary")



# funcion objetico
# Q += 3000 * (x1) + 2000 * (x2) + 7000 * (x3)
Q += (
    820 * x1
    + 810 * x2
    + 840 * x3
    + 960 * x4
    + 800 * x5
    + 870 * x6
    + 1000000 * x7
    + 920 * x8
    + 740 * x9
    + 900 * x10
    + 810 * x11
    + 840 * x12
   
)

nombres_servidores = [ "PC IPE", "PC IPM", "ET SGI", "ET SUN"]

# Restricciones de la producción
Q += 41 * x1 + 27 * x2 + 28 * x3 + 24 * x4 = 75
Q += 30 * x5 + 80 * x6 + 200 * x7 + 2000 * x8 >= 0
Q += 30 * x9 + 80 * x10 + 200 * x11 + 2000 * x12 >= 0

#Q += 30 * x1 + 80 * x2 + 200 * x3 + 2000 * x4 >= 0
#Q += 30 * x1 + 80 * x2 + 200 * x3 + 2000 * x4 >= 0
#Q += 30 * x1 + 80 * x2 + 200 * x3 + 2000 * x4 >= 0


# Q += 3 * x1 + 2 * x2 + x3 <= 600, "Restricción de agua Kibbutz 1"
# Q += 3 * x4 + 2 * x5 + x6 <= 800, "Restricción de agua Kibbutz 2"
# Q += 3 * x7 + 2 * x8 + x9 <= 375, "Restricción de agua Kibbutz 3"
#
## Restricción total de acres para cada cultivo
# Q += x1 + x4 + x7 <= 600, "Restricción total de acres para cultivo 1"
# Q += x2 + x5 + x8 <= 500, "Restricción total de acres para cultivo 2"
# Q += x3 + x6 + x9 <= 325, "Restricción total de acres para cultivo 3"


# Valores para x1


# Solucionar el problema
Q.solve()


print(f"Estado: {pulp.LpStatus[Q.status]}")
# Imprimir los valores de las variables para cada servidor en cada mes
# Imprimir los valores de las variables para cada servidor en cada mes
for i in range(1, 21):
    if i <= 4:
        print(f"{nombres_servidores[i-1]} (Servidor Mes 1 - x{i}): {pulp.value(locals()[f'x{i}'])}")
    elif 5 <= i <= 8:
        print(f"{nombres_servidores[i-5]} (Servidor Mes 2): {pulp.value(locals()[f'x{i}'])}")
        
    elif 9 <= i <= 12:
        print(f"{nombres_servidores[i-9]} (Servidor Mes 3): {pulp.value(locals()[f'x{i}'])}")
    elif 13 <= i <= 16:
        print(f"{nombres_servidores[i-13]} (Servidor Mes 4): {pulp.value(locals()[f'x{i}'])}")
    else:
        print(f"{nombres_servidores[i-17]} (Servidor Mes 5): {pulp.value(locals()[f'x{i}'])}")


# Si tienes más meses, simplemente agregas las impresiones correspondientes


print(f"Ganancia total: {int(pulp.value(Q.objective))} millones de dólares")




# print("\033[1m" + Q.name + "\033[0m")

# Status de la solución encontrada (Unfeasible, Feasible, Optimal)
# print("Status:", pulp.LpStatus[Q.status])

# Mostrar la solución óptima
# for variables in Q.variables():
#   print(f"{variables.name} = {variables.varValue}")


# Mostrar el valor de la función objetivo en el óptimo
# print(f"Valor óptimo de Z: {Q.objective.value()}")
