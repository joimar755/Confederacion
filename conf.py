{
    "nbformat": 4,
    "nbformat_minor": 0,
    "metadata": {
        "colab": {"provenance": [], "authorship_tag": "ABX9TyP/ng8gva/um3MdcaAwx1X4"},
        "kernelspec": {"name": "python3", "display_name": "Python 3"},
    },
    "cells": [
        {
            "cell_type": "markdown",
            "source": ["### **Ejemplo 1:** Programación Lineal (PL)"],
            "metadata": {"id": "k6GvBdfH_DiN"},
        },
        {
            "cell_type": "code",
            "source": [
                "# Instalación del pequete de programación lineal PuLP\n",
                "!pip install PuLP\n",
                "\n",
                "# Importar paquete de programación lineal\n",
                "import pulp",
            ],
            "metadata": {
                "colab": {"base_uri": "https://localhost:8080/"},
                "id": "FLKVRpwRgZs8",
                "executionInfo": {
                    "status": "ok",
                    "timestamp": 1724375338168,
                    "user_tz": 300,
                    "elapsed": 3991,
                    "user": {
                        "displayName": "Canek Jackson",
                        "userId": "02039282222256553882",
                    },
                },
                "outputId": "e9281116-bdb0-4436-e875-967eab1ea533",
            },
            "execution_count": 5,
            "outputs": [
                {
                    "output_type": "stream",
                    "name": "stdout",
                    "text": [
                        "Requirement already satisfied: PuLP in /usr/local/lib/python3.10/dist-packages (2.9.0)\n"
                    ],
                }
            ],
        },
        {
            "cell_type": "code",
            "source": [
                "# Definición del problema (P) y tipo de optimización (min o max)\n",
                'Q = pulp.LpProblem("Taller_1_PLAN_DE_PRODUCCIÓN", pulp.LpMaximize) # si el problema es de Minimización se debe usar pulp.LpMinimize\n',
                "\n",
                "# Definir variables de decisión (x,y)\n",
                'x1 = pulp.LpVariable("Cantidad de autos a ensamblar del modelo A", lowBound = 0, upBound = None)\n',
                'x2 = pulp.LpVariable("Cantidad de autos a ensamblar del modelo B", lowBound = 0, upBound = 3500)\n',
                '#x3 = pulp.LpVariable("Cantidad de autos a ensamblar del modelo C", lowBound = 0, upBound = None)\n',
                "\n",
                "\n",
                "# Definir función objetivo\n",
                "def F(x1,x2):\n",
                "  return  3600*x1 + 5400*x2   # Ganancia por venta de ambos modelos\n",
                "\n",
                "# Definir los recursos utilizados en función del plan de producción (x,y)\n",
                "def R2(x1,x2):\n",
                "  return  4*x1 + 2*x2     # Cantidad de puertas\n",
                "\n",
                "def R1(x1,x2):\n",
                "  return  6*x1 + 10.5*x2  # Cantidad de horas laborales\n",
                "\n",
                "# Agregar función objetivo al problema\n",
                'Q += F(x1,x2), "Ganancia por venta de ambos modelos"\n',
                "\n",
                "# Agregar restricciones al problema\n",
                'Q += R1(x1,x2) <= 60000, "[R1] Capacidad de la planta"\n',
                'Q += R2(x1,x2) <= 20000, "[R2] Disponibilidad de puertas"\n',
                "\n",
                "# Solucionar el problema\n",
                "Q.solve()\n",
                "print('\\033[1m' + Q.name + '\\033[0m')\n",
                "\n",
                "# Status de la solución encontrada (Unfeasible, Feasible, Optimal)\n",
                'print("Status:", pulp.LpStatus[Q.status])\n',
                "\n",
                "# Mostrar la solución óptima\n",
                "for variables in Q.variables():\n",
                '    print(f"{variables.name} = {variables.varValue: .0f} [autos/semana]")\n',
                "\n",
                "# Mostrar el valor de la función objetivo en el óptimo\n",
                'print(f"Ganancia por venta de autos = {pulp.value(Q.objective)/1E6: 0.2f} [MUSD/semana]")',
            ],
            "metadata": {
                "id": "OQ7_W_XqvbQJ",
                "colab": {"base_uri": "https://localhost:8080/"},
                "executionInfo": {
                    "status": "ok",
                    "timestamp": 1724375338168,
                    "user_tz": 300,
                    "elapsed": 6,
                    "user": {
                        "displayName": "Canek Jackson",
                        "userId": "02039282222256553882",
                    },
                },
                "outputId": "2b1f7ace-3f76-4855-e6f1-033110830066",
            },
            "execution_count": 6,
            "outputs": [
                {
                    "output_type": "stream",
                    "name": "stdout",
                    "text": [
                        "\u001b[1mTaller_1_PLAN_DE_PRODUCCIÓN\u001b[0m\n",
                        "Status: Optimal\n",
                        "Cantidad_de_autos_a_ensamblar_del_modelo_A =  3250 [autos/semana]\n",
                        "Cantidad_de_autos_a_ensamblar_del_modelo_B =  3500 [autos/semana]\n",
                        "Ganancia por venta de autos =  30.60 [MUSD/semana]\n",
                    ],
                }
            ],
        },
    ],
}
