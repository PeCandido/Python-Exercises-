n = int(input())
i = 1
soma = 0
valor = 1
antecessor = 0

print(valor, end=" ")
while i < n:
    soma = valor + antecessor
    print(soma, end =" ")
   
    antecessor = valor
    valor = soma
    
    i += 1



#1 1
#2 1 + 0 = 1
#3 1 + 1 = 2
#4 3 + 2 = 5
#5 5 + 3 = 8
#6 8 + 5 = 13
#7 13 + 8 = 21
#8 21 + 13 = 34
#9 34 + 21 = 55
#10 55 + 34 = 89