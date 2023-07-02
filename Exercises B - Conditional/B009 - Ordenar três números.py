from socket import AF_UNIX


a = int(input())
b = int(input())
c = int(input())

if a > c and a > b:
    aux = a
    a = c
    c = aux

elif b > c:
    aux = b
    b = c
    c = aux

if a > b:
    aux = a
    a = b
    b = aux

print(a)
print(b)
print(c)
