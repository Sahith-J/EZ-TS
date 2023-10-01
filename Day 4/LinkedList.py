class node:
    def __init__(self,z) -> None:
        self.data=z
        self.next=None
        
class cse:
    def __init__(self) :
        self.h=None

    def creat(self,x):
        if self.h==None:
            self.h=node(x)
        else:
            temp=self.h
            while temp.next:
                temp=temp.next
            temp.next=node(x)
    def insertatbeg(self,x):
        if self.h==None:
            self.h=node(x)
        else:
            temp=node(x)
            temp.next=self.h
            self.h=temp
    def display(self):
        temp=self.h
        while temp:
            print(temp.data,end="->")
            temp=temp.next

b=cse()
b.creat(10)
b.creat(20)
b.creat(30)
b.creat(40)
b.insertatbeg(5)
b.display()
# if self is there then non static method, else it is static method.
# non static variable needs object and static variable can be called from both class and object.

#print(a)
#prints the reference of the object


