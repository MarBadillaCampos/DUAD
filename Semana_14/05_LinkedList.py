
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node
    
class LinkedList:
    def __init__(self,head=None):
        self.head = head
    
    def print_all(self):
        current_node = self.head
        while current_node is not None:
            if current_node.next_node is not None:
                print(current_node.data, end=' -> ')
            else:
                print(current_node.data)
            current_node = current_node.next_node
    
    def insert_back(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next_node is not None:
            current_node = current_node.next_node
        current_node.next_node = new_node
    
    def insert_front(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next_node = self.head
        self.head = new_node
    
    def delete(self, data):
        current_node = self.head
        previous_node = None

        while current_node is not None:
            if current_node.data == data:
                if previous_node is None:
                    self.head = current_node.next_node
                    return
                else:
                    previous_node.next_node = current_node.next_node
                    return
            previous_node = current_node
            current_node = current_node.next_node


dll = LinkedList()
print("Insert front")
dll.insert_front(10)
dll.insert_front(20)
dll.print_all()

print("Insert Back")
dll.insert_back(30)
dll.print_all()
print('Delete specific Node')
dll.delete(10)
dll.print_all()

