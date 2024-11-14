
import pulp


Q = pulp.LpProblem(
    "Plantas", pulp.LpMinimize
)  # si el problema es de Minimización se debe usar pulp.LpMinimize



x1 = pulp.LpVariable("x1-1", cat="Binary")
x2 = pulp.LpVariable("x1-2", cat="Binary")
x3 = pulp.LpVariable("x1-3", cat="Binary")
x4 = pulp.LpVariable("x1-4", cat="Binary")
x5 = pulp.LpVariable("x2-1", cat="Binary")
x6 = pulp.LpVariable("x2-2", cat="Binary")
x7 = pulp.LpVariable("x2-3", cat="Binary")
x8 = pulp.LpVariable("x2-4", cat="Binary")
x9 = pulp.LpVariable("x3-1", cat="Binary")
x10 = pulp.LpVariable("x3-2", cat="Binary")
x11 = pulp.LpVariable("x3-3", cat="Binary")
x12 = pulp.LpVariable("x3-4", cat="Binary")



# funcion objetico
# Q += 3000 * (x1) + 2000 * (x2) + 7000 * (x3)
Q += (
    820 * x1
    + 810 * x2
    + 840 * x3
    + 960 * x4
    + 800 * x5
    + 870 * x6
    + 920 * x8
    + 740 * x9
    + 900 * x10
    + 810 * x11
    + 840 * x12
)



# Restricciones de la producción
# Restricciones de capacidad para cada planta
Q += 41 * x1 + 27 * x2 + 28 * x3 + 24 * x4 <= 75    # Planta 1
Q += 40 * x5 + 29 * x6 + 23 * x8 <= 75              # Planta 2
Q += 37 * x9 + 30 * x10 + 27 * x11 + 21 * x12 <= 45 # Planta 3

Q += x1 + x5 + x9 == 1   #Producto 1 debe asignarse a alguna planta
Q += x2 + x6 + x10 == 1  #Producto 2 debe asignarse a alguna planta
Q += x3 + x11 == 1       #Producto 3 debe asignarse a alguna planta
Q += x4 + x8 + x12 == 1  #Producto 4 debe asignarse a alguna planta





# Solucionar el problema
Q.solve()
for variable in Q.variables():
    print(f"{variable.name} = {variable.varValue}")

# Iterar sobre cada variable y verificar si su valor es 1


print(f"Estado: {pulp.LpStatus[Q.status]}")


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
