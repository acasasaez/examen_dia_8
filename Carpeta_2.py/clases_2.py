class Alumno():
    def __init__(self, nombre,nota):
        self.nombre = nombre
        self.nota = nota
    
    def __str__(self):
        return "Nombre: {}, Nota: {}".format(self.nombre, self.nota)

    def set_nombre(self, nombre):
        self.nombre = nombre
    def get_nombre(self):
        return self.nombre

    def set_nota(self, nota):
        self.nota = nota 
    def get_nota(self):
        return self.nota

 
