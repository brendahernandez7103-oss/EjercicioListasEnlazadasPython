"""class carro:
    def __init__(self, color, marca):
        self.color = color
        self.marca = marca

#creamos objeto (carros)
c1 = carro("rojo","toyota")
c2 = carro("azul", "nissan")
print(c1.color, c1.marca)
print(c2.color, c2.marca)"""

"""class Node: #defines como "molde" llamando Node para crear nodos
    def __init__(self, data): #es el contructor, se jecuta automaticamente cada vez que creas un objeto Node.
        self.data = data #guarda el valor que quieras en el nodo.
        self.next = None #apunta al siguiente nodo, Al inicio es None porque todavia no lo hemos enlazado

#creamos nodes
node1 = Node(15)
node2 = Node(3)
node3 = Node(17)
node4 = Node(90)
node5 = Node(22)
node6 = Node(5) 

head = node4 #head es el primer nodo de la lista enlazada

#traverse and print the linked list
current = head
while current:
    print(current.data, end="->")
    current = current.next
    print("None")"""



