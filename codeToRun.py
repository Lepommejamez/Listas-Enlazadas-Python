from ListasEnlazadas import Nodo
from ListasEnlazadas import SimpleLinkedList
from ListasEnlazadas import CircularLinkedList

lista1 = CircularLinkedList()
lista1.addNode(1)
lista1.addNode(2)
lista1.addNode(3)
lista1.addNode(4)
lista1.addNode(5)
lista1.addNode(6)

lista1.Eliminar(2)
print(lista1)