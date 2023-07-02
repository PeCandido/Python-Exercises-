n = int(input())

i = 1
soma = 0
primo = 0
while i <= n:
    j = 1
    cont = 0
    while j <= i and cont <= 2:
        if i % j == 0:
            cont += 1
        j += 1

    if cont == 2:
        primo = i

    soma += primo
    primo = 0
    i += 1

print(soma)
    