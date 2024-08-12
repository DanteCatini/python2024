def menu():
    menuI = '''
#########################################
     1 - añadir una tarea                         
     2 - ver todas las tareas                      
     3 - marcar una tarea como completada               
     4 - salir                        
######################################### 
'''
    print(menuI)
    opcion = int(input("ingrese la opcion deaseada: "))
    return opcion
def menu2():
    menuI2 = '''
################
    1 - si
    2 - no
################     
    '''
    print(menuI2)
    opcion2 = int(input("posta desea salir?: "))
    return opcion2
tareas = []
historialResultados = {}
while True:
    opcion = menu()
    if opcion == 1:
        tarea1 = input("escriba la tarea que quiera anotar: ")
        tareas.append(tarea1)
        print("tarea añadida")
        
    elif opcion == 2:
        if not tareas:
            print("no tienes tareas registradas")
        else:
            print(tareas)


    elif opcion == 3:
        if not tareas:
            print("no tienes tareas registradas")
        else:
            print(tareas)
            num_tarea = input("decida que tarea eliminar (coloque el numero en que se encuentra esta tarea):")
            if  1 <= num_tarea  == len(tareas):
                tarea_eliminada = tareas.pop(num_tarea - 1)
                print("la tarea ha sido eliminado correctamente")
            else:
                print("no hay ese numero de tarea")


    elif opcion == 4:    
        opcion2 = menu2()
        if opcion2 == 2:
            print("bien ahi")
            continue
        else:
            print("fin del programa")
        break
    else:
        print("opcion no valida")

