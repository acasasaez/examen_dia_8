class vehiculo(): 
    def __init__(self, ruedas, color):
        self.ruedas = ruedas
        self.color = color
        
    def __str__(self):
        return "X"

    def correr(self):
        print("Corriendo")

class coche(vehiculo):
    def __init__(self, ruedas, color, puertas):
        super().__init__(ruedas, color)
        self.puertas = puertas
    
    def correr(self):
        print ("Corriendo a 100km/h")

class feo (vehiculo):
    def __init__(self, ruedas, color, puertas):
        super().__init__(ruedas, color)
        self.puertas = puertas
    
    def correr(self):
        print ("Corriendo a 200km/h")

class ibiza (coche, feo):
    def __init__(self, ruedas, color, puertas, marca):
        coche.__init__(ruedas, color, puertas)
        self.marca = marca

    def correr(self):
        for i in range (5):
            super().correr()

Manolo =ibiza(4, "rojo", 5, "Seat")
Manolo.correr()