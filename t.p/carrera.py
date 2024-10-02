from personaje_clase import personaje


def menu():
    menuI = '''
#########################################
#     1 - crear personaje               #
#     2 - jugar                         #
#     3 - mostrar informacion           #
#     4 - Salir                         #
######################################### '''
    print(menuI)
    opcion = int(input("ingrese la opcion deaseada: "))
    return opcion

cantidad_personajes = 0
personajes = []

while True:
        opcion = menu()
        if opcion == 1:
            print("ingrese las caracteristicas de su personaje")
            nombre = input("Ingresa el nombre del personaje: ")
            altura = int(input("Ingresa la altura del personaje (numero entero): "))
            velocidad = int(input("Ingresa la velocidad del personaje (0 / 50): "))
            resistencia = int(input("Ingresa la resistencia del personaje (0 / 50): "))
            fuerza = int(input("Ingresa la fuerza del personaje (0 / 30): "))

            nuevo_personaje = personaje(nombre, altura, velocidad, resistencia, fuerza)
            personajes.append(nuevo_personaje)
            
            cantidad_personajes += 1
            print(f"el personaje {nuevo_personaje.nombre} ha sido creado")
            print(f"cantidad de personajes creados: {cantidad_personajes} ")

        elif opcion == 2:
            if cantidad_personajes  == 1:
                print("No hay suficientes personajes para iniciar un combate.")
            else:
            # Mostrar personajes disponibles
                print("Personajes disponibles:")
                for i, p in enumerate(personajes):
                    print(f"{i+1} - {p.nombre}")


                atacante = int(input("Seleccione el número del personaje atacante: ")) - 1
                objetivo = int(input("Seleccione el número del personaje objetivo: ")) - 1

                atacante = personajes[atacante]
                objetivo = personajes[objetivo]

                atacante.atacar(objetivo)
    
        elif opcion == 3:

            for p in personajes:
                p.mostrar_info()
    
        elif opcion == 4:

            print("Saliendo del juego...")
            break