# input : B
# output : 2

n=input()
if ord(n)>=65 and ord(n)<=90:
    print(ord(n)-ord('A')+1)
elif ord(n)>=97 and ord(n)<=122:
    print(ord(n)-ord('a')+1)