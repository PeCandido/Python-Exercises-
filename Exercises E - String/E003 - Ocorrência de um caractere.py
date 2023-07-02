palavra = input()
letra = input()

i = 0
cont = 0
while i < len(palavra):
    if palavra[i] == letra:
        cont += 1
    i += 1

print(cont)