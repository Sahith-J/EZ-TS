#ip : h 
#   : 3
# op : k 

n=input()
k=int(input())
x=ord(n)+k
if x>122:
    print(chr(x-26))
else:
    print(chr(x))