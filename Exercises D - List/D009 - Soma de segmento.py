n = int(input())
lista = list(map(int, input().split()))
i, j = list(map(int, input().split()))

menor = i
maior = j
soma = 0
cont = 0

if i > j:
    aux = menor
    menor = maior
    maior = aux

if j > len(lista) or i > len(lista) or i < 0 or j < 0:
    print("INVALIDO")

else:
    while cont <= n:
        if cont >= menor and cont <= maior:
            soma += lista[cont]
        
        cont += 1

    print(soma)

