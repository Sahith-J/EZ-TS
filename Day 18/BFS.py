# BFS 
# Queues

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def printing(self):
        if self is None:
            return
        if self.left is not None:
            self.left.printing()
        print(self.data)
        if self.right is not None:
            self.right.printing()
        
        


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

q=[]
q.append(root)

while q:
    a=q.pop(0)
    print(a.data)
    if a.left:
        q.append(a.left)
    if a.right:
        q.append(a.right)