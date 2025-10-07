#crear e imprimir
"""matriz = [
    [1,2,3]
    [4,5,6]
    [7,8,9]
]
print(matriz[0])
print(matriz[1])
print(matriz[2])
#usar un for para imprimir cada matriz
for fila in matriz:
    print(fila)
#2 interseccion
#agregar nueva fila[10,11,12] al final de la matriz
matriz.append([10,11,12])
print(matriz)
#insertar el numero 99 en la fila 0 , columna 1
matriz.insert(0,1,99)
print(matriz)
#3 eliminacion
#elimina la ultima fila usando pop
matriz.pop()
matriz[0].pop(2)
#elimina el numero 5 de la primera fila usando remove()
matriz [1].remove(5)
print(matriz)
# 4 promedio de filas
#cada fila representa calificaciones de alumnos
#calcula e imprime el promedio de cada alumno
calificaciones = [
    [100,80,90],
    [80,70,90],
    [100,85,90],
]
alumno=1
for fila in calificaciones:
    promedio = sum(fila) / len(fila)
    print("alumno ", alumno, " promedio: ", promedio)
    alumno += 1"""

#ejercicio integrador
#hacer una funcion para crear una matriz de calificaciones, retornarla por parametro
""""def crear_matriz():
    matriz = [
        [100,80,90],
        [80,90,70],
        [100,85,90]
    ]
    return matriz
def imprimir_filas(matriz):
    for fila in matriz:
        print(fila)
def calcular_promedio(matriz):
    alumnos = 1
    for fila in matriz:
        promedio = sum(fila) / len(fila)
        print("alumnos ", alumnos,  " promedio; ", promedio)
        alumnos += 1
matriz = crear_matriz()
imprimir_filas(matriz)
calcular_promedio(matriz)""""




    
