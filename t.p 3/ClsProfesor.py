import sqlite3


class Profesor:
    def __init__(self, nombre, materia, año):
        self.nombre = nombre
        self.materia = materia
        self.año = año

    def guardar(self):
        conn = sqlite3.connect('escolar.db')
        c = conn.cursor()