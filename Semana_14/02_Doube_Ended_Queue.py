#1. Debe incluir los métodos de `push_left` y `push_right` (para agregar nodos al inicio y al final) 
# y `pop_left` y `pop_right` (para quitar nodos al inicio y al final).
#2. Debe incluir un método para hacer `print` de toda la estructura.
#3. No se permite el uso de tipos de datos compuestos como `lists`,
#  `dicts` o `tuples` ni módulos como `collections`.


class Node:
  data: str
  next: "Node"

  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class double_ended_queue:
  head: Node

  def __init__(self, head):
    self.head = head

  def print_structure(self):
    current_node = self.head
    while (current_node is not None):
      print(current_node.data)
      current_node = current_node.next

  def push_left(self,new_node):
   new_node.next = self.head
   self.head = new_node

  def push_right(self, new_node):
    current_node = self.head
    next_node = current_node.next
    while (next_node is not None):
     current_node = next_node
     next_node = current_node.next
    current_node.next = new_node
 
  def pop_left(self):
   current_node = self.head
   next_node = current_node.next 
   self.head = next_node

  def pop_right(self):
    if self.head.next is None:
        value = self.head.data
        self.head = None
        return value
    
    current_node = self.head
    next_node = current_node.next
    while (next_node.next is not None):
        current_node = next_node
        next_node = next_node.next
    value = next_node.data
    current_node.next = None
    return value


third_node = Node("Soy el tercer nodo")
second_node = Node("Soy el segundo nodo", third_node)
first_node = Node("Soy el primer nodo", second_node)

double_queue = double_ended_queue(first_node)
double_queue.print_structure()

print("Agregando un elemento con push_left ")
double_queue.push_left(Node("Soy el nuevo-primero nodo!"))
double_queue.print_structure()

print("Agregando un elemento con push right")
double_queue.push_right(Node("Soy el nuevo-ultimo nodo!"))
double_queue.print_structure()

print("Eliminando un elemento con pop left")
double_queue.pop_left()
double_queue.print_structure()

print("Eliminando un elemento con pop right")
double_queue.pop_right()
double_queue.print_structure()
