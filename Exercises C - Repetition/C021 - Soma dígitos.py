n = int(input())

soma = 0
while n != 0:
    unidade = n % 10
    n = (n - unidade) // 10 
    soma += unidade

print(soma)

