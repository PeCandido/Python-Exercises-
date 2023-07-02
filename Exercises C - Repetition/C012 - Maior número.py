N = int(input())
i = 0
maior = 0

while i < N:
    x = int(input())
    if i == 0:
        maior = x

    if x > maior:
        maior = x
    i += 1

print(maior)
