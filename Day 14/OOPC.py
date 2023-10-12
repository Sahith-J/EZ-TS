# OOPC 2.0
# In Multiple InHertiance , the one which is declared first is given more priority.
#OOPC
class cse:
    def __init__(self,a) -> None:
        self.a=a
    def fun(s):
        print("fun1")
    def fun(self):
        print("fun2")

class two():
    def fun(self):
        print("fun3")
    def func4(self):
        print("fun4")

class three(cse,two):
    def fun(s):
        super().fun()
        print("fun5")


o=cse(1)
a=two()
b=three(1)
b.fun()
