posicao1 = int(input())
pulo1 = int(input())
posicao2 = int(input())
pulo2 = int(input())

iguais = "NAO"

if (posicao1 > posicao2 and pulo1 < pulo2) or (posicao1 < posicao2 and pulo1 > pulo2):
    comparacao = (posicao1 - posicao2) / (pulo2 - pulo1)
    if comparacao >= 0 and comparacao % 1 == 0:
        iguais = "SIM"
        

elif posicao1 == posicao2:
    iguais = "SIM"

print(iguais)
