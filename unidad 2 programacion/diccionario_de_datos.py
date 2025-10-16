
# Crear una lista llamada alumnos vacia
alumnos = []

# Funcion para insertar alumnos a la lista
def insertar_alumno(nombre, edad, carrera):
    """
    Funcion que recibe nombre, edad y carrera
    y crea un diccionario que se inserta en la lista alumnos
    """
    # Crear el diccionario con las claves y valores
    alumno = {
        "nombre": nombre,
        "edad": edad,
        "carrera": carrera
    }
    
    # Insertar el diccionario al final de la lista
    alumnos.append(alumno)

# Llamar a la funcion en 3 ocasiones para registrar 3 alumnos
insertar_alumno("Ana Garcia", 20, "Ingenieria Informatica")
insertar_alumno("Carlos Lopez", 22, "Medicina")
insertar_alumno("Maria Rodriguez", 19, "Derecho")

# Imprimir la lista
print("Lista de alumnos:")
print(alumnos)

