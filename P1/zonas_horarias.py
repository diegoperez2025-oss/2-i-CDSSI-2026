#INFORMACION DE EL ESTUDIANTE
#NOMBRE: DIEGO PEREZ MELESIO
#GRUPO: 2-I
#PROGRAMA:CONVERSOR DE DIVISAS Y ZONAS HORARIAS

yuan_val = 0.14
yen_val = 0.0063
euro_val = 1.16
libra_val = 1.23
mxn_val = 0.057

print("===CONVERSOR DE DIVISAS===")
pesos = float(input("ingresa la cantidad de pesos (mxn) a convertir: "))

dolares = pesos * mxn_val

print(f"\nLos ${pesos} pesos equivalen a:")
print(f"Dolares (usd): ${dolares:.2f}")
print(f"yuanes (cny): ${dolares * yuan_val:.2f}")
print(f"yenes (jpy): ${dolares * yen_val:.2f}")
print(f"euros (eur): ${dolares * euro_val:.2f}")
print(f"libras (gbp): ${dolares * libra_val:.2f}")

print("\n" + "-" * 30 + "\n")

print("---CALCULADOR DE ZONAS HORARIAS---")
print("nota: usa formato de 24 horas (0-23) para facilitar el calculo.")
hora_base = int(input("ingresa la hora actual en tu zona horaria (0-23): "))

utb = (hora_base + 6) % 24

print("\nLa hora en las siguientes ciudades seria:")
print(f"CDMX: {hora_base}:00")
print(f"dublin / londres: {(utb + 0) % 24}:00")
print(f"paris: {(utb + 1) % 24}:00")
print(f"tokio: {(utb + 9) % 24}:00")
print(f"los angeles: {(utb - 8) % 24}:00")
print(f"nueva york: {(utb - 5) % 24}:00")

print(f"nueva delhi: {(utb + 5.5) % 24}:00")