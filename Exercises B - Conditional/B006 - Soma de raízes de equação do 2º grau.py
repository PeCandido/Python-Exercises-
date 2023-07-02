import math

a = float(input())
b = float(input())
c = float(input())

delta = b**2 - (4 * a * c)
x1 = (-b + (delta * 0.5)) / (2 * a) 
x2 = (-b - (delta * 0.5)) / (2 * a) 
soma = x1 + x2

if delta >= 0:
    print(f"{soma:.2f}")

else:
    print(math.nan)