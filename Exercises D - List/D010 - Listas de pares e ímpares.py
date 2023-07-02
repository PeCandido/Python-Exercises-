n = int(input())
lista = list(map(int, input().split()))
lista_par = []
lista_impar = []

i = 0
while i < n:
    if lista[i] % 2 == 0:
        lista_par.append(lista[i])
    
    else:
        lista_impar.append(lista[i])

    i += 1

print(*lista_par)
print(*lista_impar)