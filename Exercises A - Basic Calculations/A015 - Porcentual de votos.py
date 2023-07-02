E = int(input())
B = int(input())
N = int(input())
V = int(input())

nulos = N * 100 / E
brancos = B * 100 / E
validos = V * 100 / E
ausentes = (E - (B + N + V)) * 100 / E

print(f"Nulos: {nulos:.2f}%")
print(f"Brancos: {brancos:.2f}%")
print(f"Validos: {validos:.2f}%")
print(f"Ausentes: {ausentes:.2f}%")
