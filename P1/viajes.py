#INFORMACION DE EL ESTUDIANTE
#NOMBRE: DIEGO PEREZ 
#GRUPO: 2-I
#PROGRAMA: SIMULADOR DE VIAJES
print("=== Simulador de viaje ===")

print("Seleccione destino:")
print("1 _ Estados unidos")
print("2 _ Europa")
print("3 _ japon")
print("4 _ peru")
print("5 _ medio oriente")

destino = input("selecciona el numero de tu destino: ")
edad = int(input("ingrese su edad: "))
vigencia = int(input("Años de vigilancia del pasaporte (1, 2, 5, 10): "))
if vigencia == 1:
    costo= 815
elif vigencia == 2:
    costo = 1585
elif vigencia == 5:
    costo = 2155
elif vigencia == 10:
    costo = 3780
else:
    print("vigencia no valida")
    costo = 0

if edad < 18:
    descuento = costo * 0.25
elif edad >= 60:
    descuento =costo * 0.50
else:
    descuento = 0
total = costo - descuento

if destino == 1:
    lugar = "estados unidos"
elif destino ==2:
    lugar = "europa"
elif destino == 3:
    lugar = "japon"
elif destino == 4:
    lugar = "peru"
elif destino == 5:
    lugar = "medio oriente"
else:
    lugar = "destino no valido"

print("/n== Resultado del viaje ===")
print("destino:", lugar)
print("documento requerido: pasaporte mexicano")
print("costo base:", costo, "MXN")
print("total a pagar:", total, "MXN")