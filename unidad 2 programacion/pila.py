class Stack:
    def __init__(self):
        self.items = []  # Lista interna que guarda los elementos de la pila

    def is_empty(self):
        # Devuelve True si la pila está vacía
        return len(self.items) == 0

    def push(self, item):
        # Agrega un elemento en la parte superior (tope) de la pila
        self.items.append(item)
        print(f"Se apiló: {item}")

    def pop(self):
        # Elimina y devuelve el elemento del tope de la pila
        if not self.is_empty():
            elemento = self.items.pop()
            print(f"Se desapiló: {elemento}")
            return elemento
        else:
            print("La pila está vacía, no se puede desapilar.")

    def peek(self):
        # Devuelve el elemento del tope sin eliminarlo
        if not self.is_empty():
            print(f"Elemento en el tope: {self.items[-1]}")
            return self.items[-1]
        else:
            print("La pila está vacía, no hay elemento en el tope.")

    def mostrar_pila(self):
        # Muestra el contenido completo de la pila
        print("Estado actual de la pila:", self.items)


# --- Uso de la pila paso a paso ---
pila = Stack()

print("¿La pila está vacía?", pila.is_empty())  # True

pila.push("Plato 1")      # Se apila "Plato 1"
pila.push("Plato 2")      # Se apila "Plato 2"
pila.push("Plato 3")      # Se apila "Plato 3"

pila.mostrar_pila()       # Muestra toda la pila

pila.peek()               # Muestra el elemento superior sin quitarlo

pila.pop()                # Desapila el último elemento
pila.mostrar_pila()       # Muestra la pila después de desapilar

pila.pop()                # Desapila otro
pila.pop()                # Desapila el último

pila.pop()                # Intenta desapilar cuando ya está vacía
print("¿La pila está vacía?", pila.is_empty())  # True
