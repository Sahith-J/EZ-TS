#check if the ith bit is set or not ( set means ith bit from right is 1 or not)
n=int(input())
i=int(input())
n=n&(1<<(i-1))
if n:
    print("True")
else:
    print("False")