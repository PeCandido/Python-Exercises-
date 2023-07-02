n = int(input())
lista = list(map(int, input().split()))
x = int(input())

i = 0
posição = -1
cont = 0
while i < n:
    if cont < 1:
        if x == lista[i]:
            posição = i
            cont += 1

    i += 1

print(posição)