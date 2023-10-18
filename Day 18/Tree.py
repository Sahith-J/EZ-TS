
class Node:
    def __init__(self, data):
        self.val = data
        self.right = None
        self.left = None

    def printing(self):
        if self is None:
            return
        if self.left is not None:
            self.left.printing()
        if self.right is not None:
            self.right.printing()
        print(self.val)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.printing()
