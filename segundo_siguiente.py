"""
Calcula la hora que seria, después de que pase un segundo.
"""


# Entradas
horas = int(input("Horas: "))
minutos = int(input("Horas: "))
segundos = int(input("Horas: "))

# Proceso
segundos += 1
while segundos >= 60:
    segundos = (segundos-60)
    minutos += 1
while minutos >= 60:
    minutos = (minutos-60)
    horas += 1
if horas >=24:
    horas = (horas-24)

# Salidas
print("Horas:", horas)
print("Minutos:", minutos)
print("Segundos:", segundos)
