n = int(input())
lista = list(map(int, input().split()))

i = n - 1
while i > -1:
    print(lista[i], end=' ')
    i -= 1
