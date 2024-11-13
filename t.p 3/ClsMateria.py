import sqlite3

class Materia:

    def __init__(self, nombre_materia, año_id):
        self.nombre_materia = nombre_materia
        self.año_id = año_id

    def guardar(self):
        conn = sqlite3.connect('escolar.db')
        c = conn.cursor()