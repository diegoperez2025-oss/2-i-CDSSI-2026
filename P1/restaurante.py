"""
Nombre: Diego Perez Melesio
Grupo: 2 -i
Fecha: 12/03/2026
"""
print("Restaurante")

# Creamos los contenedores de datos al inicio
menu = {}
agenda = []
ordenes = []

# Definimos las funciones (los comandos personalizados)
def agregar_platillo(nombre, precio):
    menu[nombre] = precio
    print(f"Platillo '{nombre}' agregado.")

def hacer_reservacion(nombre, fecha, hora):
    reserva = f"{nombre} - {fecha} a las {hora}"
    agenda.append(reserva)
    print(f"Reserva para {nombre} guardada.")

def tomar_orden(mesa, lista_comida):
    nueva_orden = {"Mesa": mesa, "Platillos": lista_comida}
    ordenes.append(nueva_orden)
    print(f"Orden de la mesa {mesa} enviada a cocina.")

def mostrar_todo():
    print("\n--- MENÚ ---")
    for p, pr in menu.items():
        print(f"{p}: ${pr}")
        
    print("\n--- RESERVACIONES ---")
    for r in agenda:
        print(r)
        
    print("\n--- ÓRDENES ---")
    for o in ordenes:
        print(f"Mesa {o['Mesa']}: {o['Platillos']}")

# --- EJECUCIÓN ---
agregar_platillo("Hamburguesa", 60)
agregar_platillo("Refresco", 20)
agregar_platillo("papas a la francesa", 30)
agregar_platillo("Hot dog", 40)
hacer_reservacion("Pedro pascal", "12 de Marzo", "14:00")
tomar_orden(3, ["Hamburguesa", "Papas a la francesa", "Refresco"])

mostrar_todo()