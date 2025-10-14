
# Crear una lista llamada alumnos vacía
alumnos = []

# Función para insertar alumnos a la lista
def insertar_alumno(nombre, edad, carrera):
    """
    Función que recibe nombre, edad y carrera
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

# Llamar a la función en 3 ocasiones para registrar 3 alumnos
insertar_alumno("Ana García", 20, "Ingeniería Informática")
insertar_alumno("Carlos López", 22, "Medicina")
insertar_alumno("María Rodríguez", 19, "Derecho")

# Imprimir la lista
print("Lista de alumnos:")
print(alumnos)

