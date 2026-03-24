from datetime import date

# Variables de entrada (Fecha de nacimiento)
dia_nac = 16
mes_nac = 1
año_nac = 2010

# calcular la diferencia de dias
fecha_nacimiento = date(año_nac, mes_nac, dia_nac)
fecha_actual = date.today()

# Calcular la diferencia
diferencia = fecha_actual - fecha_nacimiento
dias_vividos = diferencia.days

# Resultado
print("Calculadora de Vida")
print(f"Naciste el: (dia_nac)/(mes_nac)/(año_nac)")
print(f"Fecha de hoy: (fecha_actual)")
print(f"Has vivido exactamente: (dias_vividos) días.")