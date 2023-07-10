#Limpiar Sistema (OPCIONAL)
from os import system
system("cls")

#Importacion de...
import datetime

#Variables
total_platinum = 0
total_gold = 0
total_silver = 0
asistentes = []

#Funciones Asignadas
def mostrar_menu():
    print("************** Menú **************")
    print("1. Comprar entradas")
    print("2. Mostrar ubicaciones disponibles")
    print("3. Ver listado de asistentes")
    print("4. Mostrar ganancias totales")
    print("5. Salir")
    print("**********************************")

def comprar_entradas():
    global total_platinum, total_gold, total_silver, asistentes
    cantidad = int(input("Ingrese la cantidad de entradas a comprar (1 a 3): "))
    if cantidad < 1 or cantidad > 3:
        print("Error: cantidad inválida")
        return

    print("Las Ubicaciones disponibles:")
    mostrar_ubicaciones_disponibles()

    for i in range(cantidad):
        ubicacion = int(input("Ingrese el número de la ubicación deseada: "))
        if ubicacion < 1 or ubicacion > 100:
            print("Error: La ubicación es inválida")
            continue
        elif ubicacion in asistentes:
            print("Error: La ubicación ya no esta disponible")
            continue

        asistentes.append(ubicacion)
        if ubicacion <= 20:
            total_platinum += 1
        elif ubicacion <= 50:
            total_gold += 1
        else:
            total_silver += 1

        print("La operación se ha realizado correctamente")

def mostrar_ubicaciones_disponibles():
    print("**** Ubicaciones Disponibles *****")
    for i in range(1, 101):
        if i in asistentes:
            print("X", end=' ')
        else:
            print(i, end=' ')
        if i % 10 == 0:
            print()

def ver_listado_asistentes():
    print("***** Listado de Asistentes ******")
    asistentes.sort()
    for asistente in asistentes:
        print(asistente)

def mostrar_ganancias_totales():
    total = (total_platinum * 120000) + (total_gold * 80000) + (total_silver * 50000)
    print("******* Ganancias Totales ********")
    print("Entrada\t\tCantidad\tTotal")
    print("**********************************")
    print(f"Platinum (1-20)\t{total_platinum}\t${total_platinum * 120000}")
    print(f"Gold (21-50)\t{total_gold}\t${total_gold * 80000}")
    print(f"Silver (51-100)\t{total_silver}\t${total_silver * 50000}")
    print("**********************************")
    print(f"Total\t\t\t{total_platinum + total_gold + total_silver}\t${total}")

#El Programa principal
print("¡Bienvenido al concierto VIP de Michael Jam!")

while True:
    mostrar_menu()
    opcion = input("Ingrese una opción (1 al 5): ")

    if opcion == '1':
        comprar_entradas()
    elif opcion == '2':
        mostrar_ubicaciones_disponibles()
    elif opcion == '3':
        ver_listado_asistentes()
    elif opcion == '4':
        mostrar_ganancias_totales()
    elif opcion == '5':
        fecha_actual = datetime.date.today()
        print(f"¡Gracias por utilizar la aplicación! (Carlos Muñoz, {fecha_actual})")
        break
    else:
        print("Error: opción inválida")
        
# https://github.com/CarlosMunoz33/CarlosMunoz_PGY1121_001_D