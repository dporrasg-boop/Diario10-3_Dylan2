"""Practica Semana 07: analisis de emprendimientos costarricenses.

Complete los espacios marcados con TODO. El objetivo es generar un reporte por
sede usando listas, diccionarios, funciones, ciclos y condicionales.
"""

from sedes import sedes

def calcular_total(ventas):
    """Recibe una lista y retorna el total de ventas."""
    return sum(ventas)

print("La variable sedes es tipo:", type(sedes).__name__)
primer_emprendimiento = sedes[0]
print("primer emprendimiento", primer_emprendimiento)
print("Tipo", type(primer_emprendimiento))
print("Nombre:", primer_emprendimiento["nombre"])
print("Provincia:", primer_emprendimiento["provincia"])
print("Ventas", primer_emprendimiento["ventas"])

ventas = primer_emprendimiento["ventas"]
meta = primer_emprendimiento["meta"]

total_ventas = calcular_total(ventas)
print("Total Ventas", total_ventas)