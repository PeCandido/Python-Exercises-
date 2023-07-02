L = int(input())
M = float(input())
A = float(input())
V = int(input())
multa = 0


if V > L:
    multa = M + A * (V - L)

print(f"{multa:.2f}")
