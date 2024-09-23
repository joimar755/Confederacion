# -*- coding: utf-8 -*-
"""Ejemplo1(PL).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1i9lKXjKRQZ6RaFF6URAbfsmytFC1mmzW

### **Ejemplo 1:** Programación Lineal (PL)
"""

# Instalación del pequete de programación lineal PuLP
# pip install PuLP

# Importar paquete de programación lineal
import pulp


# Definición del problema (P) y tipo de optimización (min o max)
Q = pulp.LpProblem(
    "Taller_1_PLAN_DE_PRODUCCIÓN", pulp.LpMaximize
)  # si el problema es de Minimización se debe usar pulp.LpMinimize

# Definir variables de decisión (x,y)
x2 = pulp.LpVariable("x2", lowBound=0, upBound=None)
x1 = pulp.LpVariable("x1", lowBound=0, upBound=None)
x3 = pulp.LpVariable("x3", lowBound=0, upBound=None)

# x4 = pulp.LpVariable("x4", lowBound=0)
# x5 = pulp.LpVariable("x5", lowBound=0)
# x6 = pulp.LpVariable("x6", lowBound=0)
# x7 = pulp.LpVariable("x7", lowBound=0)
# x8 = pulp.LpVariable("x8", lowBound=0)
# x9 = pulp.LpVariable("x9", lowBound=0)

#funcion objetico
Q += 3000 * (x1) + 2000 * (x2) + 7000 * (x3)


# Restricciones de la producción
Q += 1 * x1 <= 4
Q += 2 * x2 <= 12
Q += 3 * x3 <= 15
Q += 3 * x1 + 2 * x2 + 1 * x3 <= 18


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


print("\033[1m" + Q.name + "\033[0m")

# Status de la solución encontrada (Unfeasible, Feasible, Optimal)
print("Status:", pulp.LpStatus[Q.status])

# Mostrar la solución óptima
for variables in Q.variables():
    print(f"{variables.name} = {variables.varValue}")


# Mostrar el valor de la función objetivo en el óptimo
print(f"Valor óptimo de Z: {Q.objective.value()}")
