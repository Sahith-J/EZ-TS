class Parent:
    def __init__(self):
        print("Parent constructor")

class Siva(Parent):
    def __init__(self, m1=None, m2=None):
        super().__init__() 
        if m1 is not None and m2 is None:
            print("Constructor 1")
        elif m1 is not None and m2 is not None:
            print("Constructor 2")
        else:
            print("Invalid constructor arguments")

    def __bank__(self):
        print("Test 1")

    def jeno(self):
        print("Test 2")

    def jeff(self):
        print("Test 3")

s = Siva(1)
s.jeno()
s.jeff()
s.__bank__()
