class NodoDoble:
    def __init__(self, data):
        self.data = data
        self.prev = None #apunta al nodo anterior
        self.next = None #apunta al siguiente nodo

#creamos nods
nodo1 = NodoDoble(10)
nodo2 = NodoDoble(20)
nodo3 = NodoDoble(30)

#conectar nodos
nodo1.next = nodo2
nodo2.prev = nodo1
nodo2.next = nodo3
nodo3.prev = nodo2

#cabeza de la lista
head = nodo1
current = head
while current:
    print(current.data, end="->")
    current = current.next
print("None")

#primero vamos al final
current = head
while current.next: 
    current = current.next

#recorrer hacia atras
while current:
    print(current.data, end="<-")
    current = current.prev
    print("None")
    