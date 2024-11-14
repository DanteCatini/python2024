import sqlite3

class Estudiante:
    def __init__(self, nombre, edad, año_id):
        self.nombre = nombre
        self.edad = edad
        self.año_id = año_id

    def guardar(self):
        conn = sqlite3.connect('escolar.db')
        c = conn.cursor()

        c.execute('INSERT INTO Estudiantes(nombre, edad, año_id) VALUES(?, ?, ?)',
                  (self.nombre, self.edad, self.año_id))
        
        conn.commit()
        conn.close()

    @staticmethod
    def obtener_estudiante():
        conn = sqlite3.connect('escolar.db')
        c = conn.cursor()

        c.execute('SELECT * FROM Estudiantes')
        
        estudiantes = c.fetchall()
        conn.close()

        return estudiantes
