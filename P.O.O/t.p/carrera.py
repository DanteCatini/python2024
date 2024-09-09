from personaje_clase import personaje


def menu():
    menuI = '''
#########################################
#     1 - crear personaje               #
#     2 - jugar                         #
#     3 - Salir                         #
######################################### '''
    print(menuI)
    opcion = int(input("ingrese la opcion deaseada: "))
    return opcion

cantidad_personajes = 0
personajes = []

while True:
        opcion = menu()
        if opcion == 1:
            print("ingrese las caarcteristicas de su personaje")
            nombre = input("Ingresa el nombre del personaje: ")
            altura = int(input("Ingresa la altura del personaje (numero entero): "))
            velocidad = int(input("Ingresa la velocidad del personaje (0 / 50): "))
            resistencia = int(input("Ingresa la resistencia del personaje (0 / 50): "))
            fuerza = int(input("Ingresa la fuerza del personaje (0 / 30): "))



def mostrar_info(self):
    # Método para mostrar la información del personaje
    estado = "vivo" if self.estado else "muerto"
    print(f"Personaje: {self.nombre}")
    print(f"Altura: {self.altura}")
    print(f"Velocidad: {self.velocidad}")
    print(f"Resistencia: {self.resistencia}")
    print(f"Fuerza: {self.fuerza}")
    print(f"Estado: {estado}\n")