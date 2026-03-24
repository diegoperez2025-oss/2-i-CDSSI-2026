#Datos de el usuario
from datetime import date

nombre=input("¡Hola! ¿como te llamas?:")
print(f"Mucho gusto, {nombre}. vamos a calcular unos datos interesantes sobre el calendario.")
print("\npor favor, ingresa la fecha de hoy:")
dia=int(input("dia(1-31):"))
mes=int(input("mes(1-12):"))
año=int(input("año(2026):"))

 #fecha
fecha_hoy=date(año, mes, dia)
inicio_año=date(año, 1, 1)
navidad=date(año, 12, 25)

fecha_hoy>navidad
navidad=date(año, 12, 25)

#calculos
dias_pasados=(fecha_hoy-inicio_año).days
dias_para_navidad=(navidad-fecha_hoy).days

print(f"Hoy es {fecha_hoy}.")
print(f"Han transcurrido {dias_pasados} dias desde que inicio el año.")
print(f"Faltan exactamente {dias_para_navidad}dias para navidad")
print("\n¡ya casi llega!Es momento de ir buscando los regalos. :D")