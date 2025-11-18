#1. Cree una estructura que represente una cola básica (*Queue*) con objetos enlazados
#Restricción:
#    - no usar `list`, `dict`, `tuple`, `collections`
# Métodos requeridos:
#    - `enqueue(data)`: agrega un nodo al final
#        - Ejemplo:
#            - Entrada:                
#                q.enqueue("A")
#                q.enqueue("B")
#                q.enqueue("C")                
#            - Salida:          A -> B -> C

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def print_all(self):
        current_node = self.head
        while current_node is not None:
            if current_node.next_node is not None:
                print(current_node.data, end=' -> ')
            else:
                print(current_node.data)
            current_node = current_node.next_node


class Queue(LinkedList):
    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        current_node = self.head
        while current_node.next_node is not None:
            current_node = current_node.next_node
        current_node.next_node = new_node
    
    def dequeue(self):
        if self.head is None:
            return None
        removed_node = self.head
        self.head = self.head.next_node
        return removed_node.data

q = Queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")

print("Currently Queue:")
q.print_all()
print("Delete Value:")
print(q.dequeue())
print("After delete action")
q.print_all()
