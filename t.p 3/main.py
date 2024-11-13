import sqlite3
from ClsEstudiante import Estudiante
from ClsProfesor import Profesor
from ClsCalificacion import Calificacion 
from ClsMateria import Materia

def conectar_db():
    conn = sqlite3.connect('escuela.db')
    return conn

def main():
    conn = conectar_db()
    cursor = conn.cursor()


    while True:
        print("\nSistema de Gestión Escolar")
        print("1. Agregar estudiante")
        print("2. Agregar profesor")                
        print("3. Agregar materia")
        print("4. Agregar calificación")
        print("5. Mostrar estudiantes")
        print("6. Mostrar profesores")
        print("7. Mostrar materias")
        print("8. Mostrar calificaciones")
        print("9. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            nombre = input("Nombre del estudiante: ")
            edad = input("Edad del estudiante: ")
            Estudiante.agregar(conn, nombre, edad)

        elif opcion == '2':
            nombre = input("nombre del profesor:")
            edad = input("edad del profesor: ")
            Profesor.agregar(conn, nombre, edad)

        elif opcion == '3':
            nombre = input("nombre de la materia: ")
            Materia.agregar(conn, nombre)

        elif opcion == '4':
            id_estudiante = input("id del estudiante: ")
            id_materia = input("id de la materia: ")
            nota = input("calificacion")
            Calificacion.agregar(conn, id_estudiante, id_materia, nota)

        elif opcion == '5':
            Estudiante.mostrar_todos(conn)

        elif opcion == '6':
            Profesor.mostrar_todos(conn)

        elif opcion == '7':
            Materia.mostrar_todos(conn)
        
        elif opcion == '8':
            Calificacion.mostrar_todos(conn)
            
        elif opcion == '9':
            print("saliendo del sistema....")
            break
        
        else:
            print("opcion no valida intente de nuevo")

if __name__ == "__main__":
   main()