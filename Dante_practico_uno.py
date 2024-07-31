numerosPares = []
for i in range (10):
    numeros = int(input("ingrese un numero: "))
    if numeros == 0:
        print("0 solo no es valido")
    elif numeros % 2 == 0:
        numerosPares.append(numeros)

print(numerosPares)



