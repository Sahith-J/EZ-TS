# We are entering temple. if there are 3 guards and each need 7 lemons to allow into the temple
# if normal , find how many u need
# if more than exceed, print no of extra lemons
# if negative enter valid data
# if floating enter valid lemon
# if char , pls enter valid lemon 

# do not use for , if , else , while and switch
# using ternary operator
n = input()

try:
    x = float(n)
    print("Enter Valid Data." if x < 0 else (int(x)-21) if x == int(x) and int(x)>21 else 21-int(x) if x==int(x) and int(x)<21 else "Enter Valid lemon")
except ValueError:
    print("Please enter Valid lemon." if len(n) == 1 else "Enter Valid Lemon.")






