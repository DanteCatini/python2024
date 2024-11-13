import sqlite3

class Calificacion:

    def __init__(self, estudiante, nota, año_id):
        self.estudiante = estudiante
        self.nota = nota
        self.año_id = año_id

    def guardar(self):
        conn = sqlite3.connect('escolar.db')
        c = conn.cursor()