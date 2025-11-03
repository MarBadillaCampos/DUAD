#3. Cree una estructura de objetos que asemeje un Binary Tree.
#    1. Debe incluir un método para hacer `print` de toda la estructura.
#    2. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        current_node = self.root
        while True:
            if data < current_node.data:
                if current_node.left is None:
                    current_node.left = Node(data)
                    return
                current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = Node(data)
                    return
                current_node = current_node.right

    def print_tree(self, node=None, branch=0):
        if node is None:
            node = self.root
        if node.right is not None:
            self.print_tree(node.right, branch + 1)
        print("   " * branch + str(node.data))
        if node.left is not None:
            self.print_tree(node.left, branch + 1)


bt = BinaryTree()
bt.insert(10)
bt.insert(5)
bt.insert(15)
bt.insert(2)
bt.insert(7)
bt.insert(12)
bt.insert(20)

bt.print_tree()
