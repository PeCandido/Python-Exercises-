linhas, colunas = list(map(int, input().split()))
valores = list(map(int, input().split()))

k = 0
matriz = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        x = valores[k]
        k += 1
        linha.append(x)

    matriz.append(linha)

for i in range(colunas):
    j = 0
    soma = 0
    for j in range(linhas):
        soma += matriz[j][i]
    print(soma)