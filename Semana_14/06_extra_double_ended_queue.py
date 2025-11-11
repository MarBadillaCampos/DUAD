class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def print_forward(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def print_backward(self):
        if self.head is None:
            return
        current = self.head
        while current.next is not None:
            current = current.next
        while current:
            print(current.data)
            current = current.prev

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node
        new_node.prev = current

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev is None:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                    return
                if current.next is None:
                    current.prev.next = None
                    return
                current.prev.next = current.next
                current.next.prev = current.prev
                return
            current = current.next

dll = DoubleLinkedList()
print('How to use Append')
dll.append('A')
dll.append('B')
dll.append('C')
print('Print Forward')
dll.print_forward()
print('Print Backward')
dll.print_backward()

print('How to use Prepend')
dll.prepend('E')
dll.prepend('F')
print('Print Forward')
dll.print_forward()
print('Print Backward')
dll.print_backward()



print('How to use Delete')
dll.delete('A')
print('Print Forward')
dll.print_forward()
print('Print Backward')
dll.print_backward()