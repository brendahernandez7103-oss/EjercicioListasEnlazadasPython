"""#funcion que imprima tu nombre
print("mi nombre es brenda")
#funcion que imrpima linea de asteriscos 
print("****************")
#funcion que muestre un mensaje motivacional
print("sigue adelante y no te rindas")
#funcion que reciba un nombre y lo salude
def saludar(nombre):
    print("hola " + nombre)
saludar("brenda")
#Funcion que reciba 2 numeros e imprima su suma 
def suma(a,b):
    return a + b
#funcion que valide si una persona es mayor de edad o no
def mayor_de_edad(edad):
    if edad>=18:
        print("es mayor de edad")
    else:
        print("es menor de edad")
mayor_de_edad(int(input("ingrese su edad: ")))

#funcion que reciba 2 numeros y retorne su multiplicacion
def multipliplicacion(a,b):
    return a * b


#funcion que reciba un texto y retorne cuantas letras tiene 
def contar_letras(texto):
    return len(texto)
def lonjituf(texto):
    texto=input("ingresa un texto: ")
    print("el texto tiene " + str(contar_letras(texto)) + " letras")"""

# Integrando funciones: Calculadora básica

#unción principal que implementa la calculadora basica
print("CALCULADORA BÁSICA") 
    
    # Pedir por teclado dos números y convertirlos a float

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
    
    # Mostrar menú de operaciones
print("\nOperaciones disponibles:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
    
    # Pedir selección de operación
opcion = input("\nSelecciona una operación (1-4): ")
    
    # Realizar la operación seleccionada
if opcion == "1":
        resultado = (num1 + num2)
        print(f"\n{num1} + {num2} = {resultado}")
    
elif opcion == "2":
        resultado = (num1 - num2)
        print(f"\n{num1} - {num2} = {resultado}")
    
elif opcion == "3":
        resultado = (num1 * num2)
        print(f"\n{num1} × {num2} = {resultado}")
    
elif opcion == "4":
        resultado = (num1 / num2)
        print(f"\n{num1} ÷ {num2} = {resultado}")
else:
        print("Opción no válida")
#Funcion "ingresar_palabras" pedira palabras con un ciclo hasta que se ingrese la palabra "fin"
def ingresar_palabras():
        palabras = []
        while True:
                palabra=input("ingrese una palabra o 'fin' para terminar: ")
                if palabra.lower() == "fin":
                        break
                palabras.append(palabra)
                return palabras
lista_palabras1 = ingresar_palabras()
print("palabras ingresadas: ",lista_palabras1)
def contar_palabras(palabras):
        return len(palabras)
print("contar palabras: " , contar_palabras(lista_palabras1))



