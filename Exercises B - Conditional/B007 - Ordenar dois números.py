a = int(input())
b = int(input())

if a > b:
    aux = a
    a = b
    b = aux

print(a)
print(b)
