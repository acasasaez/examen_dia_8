import clases_2
Maria = clases_2.Alumno("Maria", 8)
Juan = clases_2.Alumno("Juan", 6)
Ruben = clases_2.Alumno("Ruben", 10)





def inicio():
    print("Si quieres saber la nota de un alumno, introduce su nombre")
    nombre = input(">")
    if nombre == Maria.get_nombre():
        Maria.notas()
    elif nombre == Juan.get_nombre():
        Juan.notas()
    elif nombre == Ruben.get_nombre():
        Ruben.notas()
    else:
        print("No se ha encontrado el alumno")
        inicio()