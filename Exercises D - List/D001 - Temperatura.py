temp = list(map(int, input().split()))

soma = 0
i = 0
while i < 7:
    soma += temp[i]
    i += 1

media = soma / 7

cont_temp = 0
j = 0
while j < 7:
    if temp[j] > media:
        cont_temp += 1
    j += 1

print(cont_temp)
