idade = int(input())
maior = 0
soma = 0
n = 0
velho = 0

while idade >= 0:
    n += 1
    soma += idade

    if idade >= 18:
        maior += 1

    if idade > 75:    
        velho += 1

    idade = int(input())
        
media = soma / n
idoso = (velho / n) * 100
    
print(f"{media:.2f}")
print(maior)
print(f"{idoso:.2f}%")