class node:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.prev = None

class dll:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertatbeg(self, data):
        if self.head is None:
            new_node = node(data)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = node(data)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def printx(self):
        temp = self.head
        while temp:
            print(temp.val, end=" -> ")
            temp = temp.next

        print() 
        temp1 = self.tail
        while temp1:
            print(temp1.val, end=" -> ")
            temp1 = temp1.prev
        print()  

    def insertatend(self, data):
        if self.head is None:
            new_node = node(data)
            self.head = new_node
            self.tail = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next

            new_node = node(data)
            temp.next = new_node
            new_node.prev = temp
            self.tail = new_node  

    def delatend(self):
        if self.head is None:
            return None
        elif self.head.next is None:
            valx = self.head.val
            self.head = None
            self.tail = None
            return valx
        else:
            temp = self.head
            while temp.next.next:
                temp = temp.next
            valx = temp.next.val
            temp.next = None
            self.tail = temp  
            return valx

    def delatbeg(self):
        if self.head is None:
            return None
        else:
            valx = self.head.val
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            return valx

l = [2, 4, 6, 8, 9]
o = dll()
for i in l:
    o.insertatend(i)

o.printx()
