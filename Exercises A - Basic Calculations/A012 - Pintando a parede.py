import math
l = float(input())
a = float(input())
c = float(input())
m = float(input())

area = l * a
latas = area / m 
latas2 = math.ceil(latas)
custo = latas2 * c

print(latas2)
print(f"{custo:.2f}")
