from re import I


N = int(input())
maior = 0
menor = 0
soma = 0
i = 0

while i < N:
    x = int(input())

    if i == 0:
        maior = x
        menor = x
    
    if x > maior:
        maior = x

    if x < menor:
        menor = x
    
    soma += x
    i += 1

print(maior)
print(menor)
print(soma)
