import clases_3
Maria = clases_3.Alumno("Maria", 8)
Juan = clases_3.Alumno("Juan", 6)
Ruben = clases_3.Alumno("Ruben", 10)

def inicio():
    print("A continuación mostramos los alumnos y sus notas")
    print(Maria.__str__())
    print(Juan.__str__())
    print (Ruben.__str__())