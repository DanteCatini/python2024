from Personaje_ import Personaje

def menu():
    menuI = '''
#########################################
#     1 - crear personaje               #
#     2 - mostrar caracteristicas       #
#     3 - Salir                         #
######################################### '''
    print(menuI)
    opcion = int(input("ingrese la opcion deaseada: "))
    return opcion

cantidad_personajes = 0

while True:
    opcion = menu()
    if opcion == 1:
        cantidad_personajes = cantidad_personajes + 1
        print("ingrese las caarcteristicas de su personaje")
        nombre = input("Ingresa el nombre del personaje: ")
        altura = int(input("Ingresa la altura del personaje (número entero): "))
        velocidad = int(input("Ingresa la velocidad del personaje (número entero): "))
        resistencia = int(input("Ingresa la resistencia del personaje (número entero): "))
        fuerza = int(input("Ingresa la fuerza del personaje (número entero): "))

    elif opcion == 2:
        print(f"el nombre de tu personaje es:{cantidad_personajes.nombre}")
        print(f"la altura de tu personaje es:{cantidad_personajes.altura}")
        print(f"la velocidad de tu personaje es:{cantidad_personajes.velocidad}")
        print(f"la resistencia de tu personaje es:{cantidad_personajes.resistencia}")
        print(f"el nombre de tu personaje es:{cantidad_personajes.fuerza}")
    
    elif opcion == 3:
        print("fin del programa")
        break

#mi_personaje = Personaje(nombre, altura, velocidad, resistencia, fuerza )

#print(f"el nombre de tu personaje es:{mi_personaje.nombre}")
#print(f"la altura de tu personaje es:{mi_personaje.altura}")
#print(f"la velocidad de tu personaje es:{mi_personaje.velocidad}")
#print(f"la resistencia de tu personaje es:{mi_personaje.resistencia}")
#print(f"el nombre de tu personaje es:{mi_personaje.fuerza}")

#mi_personaje2 = Personaje(nombre, altura, velocidad, resistencia, fuerza )

#print(f"el nombre de tu personaje es:{mi_personaje.nombre}")
#print(f"la altura de tu personaje es:{mi_personaje.altura}")
#print(f"la velocidad de tu personaje es:{mi_personaje.velocidad}")
#print(f"la resistencia de tu personaje es:{mi_personaje.resistencia}")
#print(f"el nombre de tu personaje es:{mi_personaje.fuerza}")