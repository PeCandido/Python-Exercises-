n = int(input())

i = 1
sequencia = 1
maior_seq = 1
num = int(input())
while i < n:
    prox_num = int(input())

    if prox_num >= num:
        sequencia += 1
    
    if sequencia > 1 and prox_num < num:
        sequencia = 1

    if sequencia > maior_seq:
        maior_seq = sequencia
    num = prox_num

    i += 1

print(maior_seq)
    
