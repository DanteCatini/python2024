palabra = input("escriba una contrasena: ")
listaContrasena = []

for i in palabra:
        print("*", end="")
        listaContrasena.append(i)
print() 
print(listaContrasena)
listaContrasena.pop(4)        
print(listaContrasena)