n = int(input())
lista = list(map(int, input().split()))

maior = lista[0]

i = 0
cont = 0
while i < n:
    if lista[i] > maior:
        maior = lista[i]
        cont = i

    i += 1

print(maior)
print(cont)
