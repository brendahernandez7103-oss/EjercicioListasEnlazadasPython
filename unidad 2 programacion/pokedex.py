# 1.Definir una lista vacía
lista_pokemon = []

# 2.Hacer 3 funciones:

# a.Función para agregar Pokémon
def agregar_pokemon():
    print("\n  AGREGAR POKÉMON ")
    nombre = input("Ingresa el nombre del Pokémon: ")
    tipo = input("Ingresa el tipo del Pokémon: ")
    ps = input("Ingresa los PS (Puntos de Salud) del Pokémon: ")
    
    # Crear diccionario con los datos del Pokémon
    pokemon = {
        "nombre": nombre,
        "tipo": tipo,
        "ps": ps
    }
    
    # Insertar en la lista global
    lista_pokemon.append(pokemon)
    print(f"¡{nombre} ha sido agregado a la poquedex!")

# b. Función para ver todos los pokemones
def ver_pokemones():
    print("\n POKÉMONES EN LA POQUEDEX")
    
    if len(lista_pokemon) == 0:
        print("No hay Pokémon en la poquedex.")
    else:
        # Usando un for para mostrar todos los elementos
        for i, pokemon in enumerate(lista_pokemon, 1):
            print(f"{i}. Nombre: {pokemon['nombre']} | Tipo: {pokemon['tipo']} | PS: {pokemon['ps']}")

# c. Función para eliminar un pokemon
def eliminar_pokemon():
    print("\n ELIMINAR Pokemon ")
    if len(lista_pokemon) == 0:
        print("no hay pokemon en la poquedex para eliminar")
        return
    ver_pokemones()
    try:
        numero = int(input("ingressar el numero del pokemon que desea eliminar: "))
        if 1 <= numero <= len(lista_pokemon):
            eliminado = lista_pokemon.pop(numero - 1)
            print(f"¡{eliminado['nombre']} ha sido eliminado de la poquedex!")
        else:
            print("Número inválido. Por favor, intenta de nuevo.")
    except ValueError:
        print("Entrada inválida. Por favor ingresa un número entero.")
    

# 3.flujo principal con while para mostrar menu
def Mostrar_menu():

    while True:
        print("\n POQUEDEX MENU ")
        print("1. Agregar Pokémon")
        print("2. Ver Pokémons")
        print("3. Eliminar Pokémon")
        print("4. Salir")
        
        opcion = input("Selecciona una opción (1-4): ")
        
        if opcion == '1':
            agregar_pokemon()
        elif opcion == '2':
            ver_pokemones()
        elif opcion == '3':
            eliminar_pokemon()
        elif opcion == '4':
            print("¡Gracias por usar la poquedex! ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, intenta de nuevo.")

#ejecutar el proograma
Mostrar_menu()
