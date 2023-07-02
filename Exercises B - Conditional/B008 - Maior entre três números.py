a = int(input())
b = int(input())
c = int(input())

if a > b and a > c:
    maior = a

elif b > a and b > c:
    maior = b

else:
    maior = c

print(maior)
