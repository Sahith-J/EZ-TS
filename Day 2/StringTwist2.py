# hello, how is your family?!
# Constraint 1 : I won't disturb white spaces and special characters
# Constraint 2 : reverse based on input word length 
# Output : ylima , fru oy siwo holleh?!

s1=input()
l2=list()
Map={} # Index : Symbol
# Index is Key and Symbol is Value
s = '[@_!#$%^&*()<>?/\|}{~:],'
for i in range(len(s1)):
    if s1[i]==" ":
        Map[i]=s1[i]
    if s1[i] in s:
        Map[i]=s1[i]
s3=str()
for c in s1:
    if c.isalnum():
        s3=s3+c
s3=s3[::-1]
l1=list(s3.split())
s2=str()
for c in s3:
    s2=s2+c
for i in Map.keys():
    s2=s2[:i]+Map[i]+s2[i:]
print(s2)


