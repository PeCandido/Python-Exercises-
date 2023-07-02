n = int(input())
i = 1
fat = 1
soma = 0
fat0 = 1
soma0 = 1

if n != 0:
    while i <= n:
        fat = fat * i
        soma = soma + fat
        soma0 = soma + 1
        i += 1

print(soma0)   


