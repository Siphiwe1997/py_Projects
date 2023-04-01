import math
#Find the combination of the pythegoras numbers

max_n = int(input('Enter max numbers: '))
for a in range(1, max_n+1):
    for b in range(a, max_n):
        c_squared = a ** 2 + b ** 2
        c = int(math.sqrt(c_squared))
        if (c_squared - c**2) == 0:
            print(a, b, c)
