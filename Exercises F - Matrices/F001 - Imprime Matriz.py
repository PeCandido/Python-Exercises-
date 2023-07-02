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

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end= ' ')
    print()

