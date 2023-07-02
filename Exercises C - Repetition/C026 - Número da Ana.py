n = int(input())
a = 0
b = 1
c = 2
mult = 0

while mult < n:
    
    mult = a * b * c

    a += 1
    b += 1
    c += 1

if mult == n:
    print("S")

else:
    print("N")