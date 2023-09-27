#Magical Prime 17 prime 71 prime so both magical prime implement in bank 
# Neon Number Program -- sum of digits of it's square is equal to no then it;s neon check from 0 to 100 in jewels method

def magical_prime(n):
    str1=str(n)
    str2=str1[::-1]
    n1=int(str2)
    if is_prime(n)==1 and is_prime(n1)==1:
        print("Yes")
    else:
        print("No")
def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return 0
    return 1
    



def checkNeon (x) :
    sq = x * x
    sum_digits = 0
    while (sq != 0) :
        sum_digits = sum_digits + sq % 10
        sq = sq / 10
    return (sum_digits == x)
i = 1
while i <= 10000 :
    if (checkNeon(i)) :
        print (i),
    i = i + 1

magical_prime(14)