class Padre():
    def __init__(self, nombre, apellido, color_pelo):
        self.nombre = nombre
        self.apellido = apellido
        self.color_pelo = color_pelo

    def comer(self):
        print("Estoy comiendo")

class Madre():
    def __init__(self, nombre, apellido, color_ojos):
        self.nombre = nombre
        self.apellido = apellido
        self.color_ojos = color_ojos
    
    def comer(self):
        print("Ya he comido")

class Hijo(Padre, Madre):
    def __init__(self, nombre, apellido, color_pelo, color_ojos, edad):
        Padre.__init__(self, nombre, apellido, color_pelo)
        Madre.__init__(self, nombre, apellido, color_ojos)
        self.edad = edad
    def __str__(self):
        return "Nombre: {}, Apellido: {}, Color de pelo: {}, Color de ojos: {}, Edad: {}".format(self.nombre, self.apellido, self.color_pelo, self.color_ojos, self.edad)

    def comer(self):
        super.comer()

mi_hijo = Hijo("Juan", "Perez", "Castaño", "Verdes", 12)

mi_hijo.comer()
