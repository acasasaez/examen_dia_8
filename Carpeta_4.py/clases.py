


class producto ():
    def __init__ (self, codigo, nombre, precio, tipo):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo

    def set_codigo(self, codigo):
        self.codigo = codigo
    def get_codigo(self):
        return self.codigo

    def set_nombre(self, nombre):
        self.nombre = nombre
    def get_nombre(self):
        return self.nombre

    def set_precio(self, precio):
        self.precio = precio
    def get_precio(self):
        return self.precio

    def set_tipo(self, tipo):
        self.tipo = tipo
    def get_tipo(self):
        return self.tipo

    def __str__(self):
        return f"Nuestro producto tiene: Codigo: {self.codigo}/n, Nombre: {self.nombre}, Precio: {self.precio}, Tipo: {self.tipo}"
       

hola = producto(1, "hola", 2, "tipo")
print(hola.__str__())