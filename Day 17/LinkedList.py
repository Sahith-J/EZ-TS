#Linked List

# Node is object having 2 values in Python 
class node:
    def __init__(self,val=0):
        self.val=val
        self.next=None

class sll:
    def __init__(self):
        self.head=None
    def insertatbeg(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            temp=node(data)
            temp.next=self.head
            self.head=temp


    def printx(self):
        temp=self.head
        while temp:
            print(temp.val,end=" -> ")
            temp=temp.next

    def insertatend(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            temp=self.head
            while temp.next:
                temp=temp.next   
            temp.next=node(data)


    def delatend(self):
        if self.head==None:
            return 
        elif self.head.next==None:
            self.head=None
            return None
            
        else:
            temp=self.head
            while temp.next.next:
                temp=temp.next
            valx=temp.next.val
            temp.next=None
            return valx
        
    def delatbeg(self):
        if self.head==None:
            return None
        else:
            temp=self.head
            self.head=self.head.next
            temp.next=None
            return temp.val
            

l=[2,4,6,8,9]
o=sll()
o.insertatbeg(1)
print(o.delatend())
print(o.delatbeg())
o.printx()

"""
o1=node(1)
o1.next=node(2)
o1.next.next=node(3)
#print(o1.val,o1.next.val,o1.next.next.val)
"""


