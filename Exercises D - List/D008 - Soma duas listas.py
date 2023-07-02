n = int(input())
lista_a = list(map(int, input().split()))
lista_b = list(map(int, input().split()))
lista_c = []

i = 0
soma = 0
while i < n:
    soma = lista_a[i] + lista_b[i]
    lista_c.append(soma)
    
    print(lista_c[i], end=' ')
    i += 1


