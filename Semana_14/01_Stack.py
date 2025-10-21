#1. Cree una estructura de objetos que asemeje un Stack.
#    1. Debe incluir los métodos de `push` (para agregar nodos) y `pop` (para quitar nodos).
#    2. Debe incluir un método para hacer `print` de toda la estructura.
#    3. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` 
# ni módulos como `collections`.

class Node:
  data: str
  next: "Node"

  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class Stack:
  head: Node

  def __init__(self, head):
    self.head = head

  def print_structure(self):
    current_node = self.head
    while (current_node is not None):
      print(current_node.data)
      current_node = current_node.next

  def push(self,new_node):
   new_node.next = self.head
   self.head = new_node
   



  def pop(self):
   current_node = self.head
   next_node = current_node.next
   self.head = next_node
   



third_node = Node("Soy el tercer nodo")
second_node = Node("Soy el segundo nodo", third_node)
first_node = Node("Soy el primer nodo", second_node)

linked_list = Stack(first_node)
linked_list.print_structure()

print("Agregando un elemento")
linked_list.push(Node("Soy el nuevo nodo!"))
linked_list.print_structure()

print("Eliminando un elemento")
linked_list.pop()
linked_list.print_structure()

