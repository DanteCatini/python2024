class personaje :
    estado = True #vivo
    vida = 100 #cantidad de vida
    
    def __init__(self, nombre, altura, velocidad, resistencia, fuerza):
        self.nombre = nombre
        self.altura = altura
        self.velocidad = velocidad
        self.resistencia = resistencia
        self.fuerza = fuerza
        self.estado = personaje.estado
        self.vida = personaje.vida

    def atacar(self, otro_personaje ):
        if self.estado :
            dano = self.fuerza - (otro_personaje.resistencia)
            print(f"{self.nombre} ataca a {otro_personaje.nombre} causando {dano}")
            otro_personaje.recibir_dano(dano)
        else:
            print(f"{self.nombre} esta muerto y no puede atacar")
        

    def recibir_dano(self, cantidad):
        if self.estado:
            self.vida = self.vida - cantidad
            print(f"{self.nombre} recibe {cantidad} de danio. vida restante {self.vida}")
            if self.vida <= 0:
                self.vida = 0
                print(f"{self.nombre} ha muerto")
        else: 
            print(f"{self.nombre} ya esta muerto")

    def mostrar_info(self):
# Metodo para mostrar la información del personaje
        estado = "vivo" if self.estado else "muerto"
        print(f"Personaje: {self.nombre}")
        print(f"Altura: {self.altura}")
        print(f"Velocidad: {self.velocidad}")
        print(f"Resistencia: {self.resistencia}")
        print(f"Fuerza: {self.fuerza}")
        print(f"Estado: {self.estado}")
        