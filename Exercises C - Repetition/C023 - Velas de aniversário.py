a = int(input())
maior = 0
contv = 0
i = 0

while i < a:
    vela = int(input())
    
    if vela > maior:
        maior = vela
        contv = 1

    elif vela == maior:
        contv += 1

    i += 1

print(contv)