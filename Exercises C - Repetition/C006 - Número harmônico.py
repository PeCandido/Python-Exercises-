N = int(input())
i = 1
soma = 0
while i <= N:
    H = 1 / i
    soma = soma + H
    i += 1

print(f"{soma:.4f}")
