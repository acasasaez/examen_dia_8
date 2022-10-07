import clases
producto_1 = clases.producto(777, "Jaja", "2 euros", "alfajor")
def inicio():
    print ("Mostramos las caricticas iniciales de nuestro producto")
    print (producto_1.__str__())
    producto_1.set_codigo(69)
    print("Ahora mostramos las caricticas del producto con el codigo modificado")
    print (producto_1.__str__())