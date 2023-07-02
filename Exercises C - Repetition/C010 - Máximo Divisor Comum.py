a = int(input())
b = int(input())
i = 1

if a > b:
    maior = a
    menor = b

else:
    maior = b
    menor = a

while menor != 0:
    divisor = menor
    menor = maior % menor
    maior = divisor 

print(divisor)


