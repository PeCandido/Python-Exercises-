n = int(input())
i = 0
maior1 = int(input())
maior2 = int(input())


if maior2 > maior1:
    aux = maior1
    maior1 = maior2
    maior2 = aux

while i < (n - 2):
    num = int(input())

    if num > maior1:
        maior2 = maior1
        maior1 = num

    elif num > maior2:
        maior2 = num


    i += 1

print(maior1)
print(maior2)
