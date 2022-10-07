import clases_2
Maria = clases_2.Alumno()
Juan = clases_2.Alumno()
Ruben = clases_2.Alumno()

alumno_1.set_nombre("Maria")
alumno_1.set_nota(7)
alumno_2.set_nombre("Juan")
alumno_2.set_nota(4)
alumno_3.set_nombre("Ruben")
alumno_3.set_nota(10)

def notas(alumno):
    if alumno.get_nota() < 5:
        return "Suspenso"
    elif alumno.get_nota() < 7:
        return "Aprobado"
    elif alumno.get_nota() < 9:
        return "Notable"
    else:
        return "Sobresaliente"

def inicio():
    print("

