# I want to find the perfect square numbers in the range 40 to 100
'''
for i in range (40, 101):
        j = 1
        while j * j <= i:
            if j * j == i:
                 print(i)
            j = j + 1
        i = i + 1

'''




print([i for i in range(40,101) if int(i**0.5)**2==i])

