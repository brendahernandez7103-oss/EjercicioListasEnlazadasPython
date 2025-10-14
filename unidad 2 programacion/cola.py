class Queue:
    def __init__(self):
        # La lista interna representará la cola
        self.items = []

    def is_empty(self):
        # Devuelve True si la cola está vacía
        return len(self.items) == 0

    def enqueue(self, item):
        # Agrega un elemento al final de la cola
        self.items.append(item)
        print(f"Se encoló: {item}")

    def dequeue(self):
        # Elimina y devuelve el primer elemento de la cola
        if not self.is_empty():
            elemento = self.items.pop(0)
            print(f"Se desencoló: {elemento}")
            return elemento
        else:
            print("La cola está vacía, no se puede desencolar.")

    def front(self):
        # Devuelve el primer elemento sin eliminarlo
        if not self.is_empty():
            print(f"Primer elemento en la cola: {self.items[0]}")
            return self.items[0]
        else:
            print("La cola está vacía, no hay elemento en el frente.")

    def mostrar_cola(self):
        # Muestra todo el contenido de la cola
        print("Estado actual de la cola:", self.items)


# --- Uso paso a paso de la cola ---
cola = Queue()

print("¿La cola está vacía?", cola.is_empty())  # True

cola.enqueue("Persona 1")     # Entra la persona 1
cola.enqueue("Persona 2")     # Entra la persona 2
cola.enqueue("Persona 3")     # Entra la persona 3

cola.mostrar_cola()           # Muestra toda la cola

cola.front()                  # Muestra quién está al frente sin quitarlo

cola.dequeue()                # Sale la persona 1
cola.mostrar_cola()           # Muestra la cola después de desencolar

cola.dequeue()                # Sale la persona 2
cola.dequeue()                # Sale la persona 3

cola.dequeue()                # Intenta sacar cuando ya está vacía
print("¿La cola está vacía?", cola.is_empty())  # True

