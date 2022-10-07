import clases
mi_coche = clases.coche("rojo", 4, 150, 1300)
mi_bicicleta = clases.bicicleta("azul", 2, "urbana")
mi_camion = clases.camion("blanco", 6, 1000)
mi_motocicleta = clases.motocicleta("negra", 2, 180, 600)
mis_vehiculos = [mi_coche, mi_bicicleta, mi_camion, mi_motocicleta]

def catalogar(ListaVehiculos):
    for vehiculo in ListaVehiculos:
       print(vehiculo.__str__()) 



def catalogar_2 (ListaVehiculos, ruedas):
    ListaVehiculos2 = []
    for vehiculo in ListaVehiculos:
        if vehiculo.get_ruedas() == ruedas:
            ListaVehiculos2.append(vehiculo)
    return f"Se han encontrado {len(ListaVehiculos2)} vehículos con {ruedas} ruedas"
        

def inicio():
    print("Bienvenido al catálogo de vehículos")
    print("1. Mostrar todos los vehículos")
    print("2. Mostrar vehículos con 2 ruedas")
    print("3. Mostrar vehículos con 4 ruedas")
    print("4. Mostrar vehículos con 6 ruedas")
    print("5. Salir")
    opcion = int(input("Elige una opción: "))
    if opcion == 1:
        catalogar(mis_vehiculos)
    elif opcion == 2:
        print(catalogar_2(mis_vehiculos, 2))
    elif opcion == 3:
        print(catalogar_2(mis_vehiculos, 4))
    elif opcion == 4:
        print(catalogar_2(mis_vehiculos, 6))
    elif opcion == 5:
        print("Hasta pronto")
    else:
        print("Opción incorrecta")
        inicio()