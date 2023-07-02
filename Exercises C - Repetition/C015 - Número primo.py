n = int(input())
i = 1
resto = 0
cont = 0

while i <= n:
    resto = n % i

    if resto == 0:
        cont += 1

    i += 1

if cont == 2:
    print(1)

else:
    print(0)