n = int(input())

Crescente = True
Decrescente = True
num1 = int(input())

i = 1
while i < n:
    num2 = int(input())
    if num2 > num1:
        Decrescente = False
    elif num2 < num1:
        Crescente = False
    num1 = num2
    i += 1

if Crescente == True and Decrescente == True:
    ordem = 1    
elif Crescente == True:
    ordem = 1      
elif Decrescente == True:
    ordem = -1
else:
    ordem = 0
print(ordem)   