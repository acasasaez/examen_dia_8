import clases_2
Maria = clases_2.Alumno("Maria", 8)
Juan = clases_2.Alumno("Juan", 6)
Ruben = clases_2.Alumno("Ruben", 10)



def notas(alumno):
    if alumno.get_nota() < 5:
        print("Suspenso") 
    elif alumno.get_nota() < 7:
        print ("Aprobado")
    elif alumno.get_nota() < 9:
        print ("Notable")
    else:
        print ("Sobresaliente")

def inicio():
    print("Si quieres saber la nota de un alumno, introduce su nombre")
    nombre = input(">")
    if nombre == Maria.get_nombre():
        notas(Maria)
    elif nombre == Juan.get_nombre():
        notas(Juan)
    elif nombre == Ruben.get_nombre():
        notas(Ruben)
    else:
        print("No se ha encontrado el alumno")
        inicio()