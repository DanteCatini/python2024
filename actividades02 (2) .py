def menu():
    menuI = '''
#########################################
#     1 - Calcular Area Triangulo       #
#     2 - Calcular Area Rectangulo      #
#     3 - Salir                         #
######################################### '''
    print(menuI)
    opcion = int(input("ingrese la opcion deaseada: "))
    return opcion

while True:
    opcion = menu()
    if opcion == 1:
        baseTriangulo = float(input("ingrese la base del su traingulo: "))
        alturaTriangulo = float(input("ingrese la altura del su traingulo: "))
        area = alturaTriangulo * baseTriangulo / 2
        print(f"el area de su traingulo es igual a {area}")
    elif opcion == 2:
        baseRectangulo = float(input("ingrese la base de su rectangulo: "))
        alturaRectangulo = float(input("ingrese la altura de su rectangulo: "))
        areaRectangulo = baseRectangulo * alturaRectangulo
        print(f"el area de su rectangulo es igual a {baseRectangulo}")
    elif opcion == 3:
        print("a salido con exito")
        break
    else:
        print("fin por error de opciones")

print("fin")


