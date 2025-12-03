
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
    

    def bubble_sort(self):
        if self.head is None:
            return
        
        current = self.head
        while current is not None:
            next_node = current.next_node

            while next_node is not None:
                current_value = current.data
                next_value = next_node.data
                if current_value > next_value:
                    current.data = next_value
                    next_node.data = current_value
                next_node = next_node.next_node
                
            current = current.next_node

dll = LinkedList()
print("Insert Back")
dll.insert_back(18)
dll.insert_back(-11)
dll.insert_back(68)
dll.insert_back(6)
dll.insert_back(32)
dll.insert_back(53)
dll.insert_back(-2)
dll.bubble_sort()
dll.print_all()




