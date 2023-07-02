import math
n = float(input())
c = float(input())
m = float(input())

embalagens = math.trunc(n // c)
chocolates = embalagens

while embalagens >= m:
    embalagens -= m
    embalagens += 1
    chocolates += 1  

print(chocolates)
