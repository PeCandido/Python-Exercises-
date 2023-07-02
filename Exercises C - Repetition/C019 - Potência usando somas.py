a = int(input())
b = int(input())
soma = 0
base = a


if b == 0:
    soma = 1

elif b == 1:
    soma = a

else:
    j = 1
    while j <= (b-1): 
        soma = 0
        i = 1
        while i <= a:
            soma += base
            i += 1
    
        base = soma
    
        j += 1

print(soma)
