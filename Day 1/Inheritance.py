class Siva:
    def gold(w):
        print("price 5L")
    def car(w):
        print("price 3L")
class Baby1(Siva):
    def bank(w):
        print("deposisted 2L")
class Baby2(Siva):
    def jewels(w):
        print("price 10L")
class GBaby(Baby1,Baby2):
    def hello(w):
        print("hello")


'''
b1=Baby1()
b1.bank()
b1.car()
b1.gold()
'''
b2=Baby2()
b2.jewels()
b2.car()
b2.gold()

b3=GBaby()
b3.car()
b3.gold()
b3.hello()
b3.bank()
b3.jewels()

