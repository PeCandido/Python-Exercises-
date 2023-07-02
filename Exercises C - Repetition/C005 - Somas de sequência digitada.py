i = 1
spar = 0
simpar = 0
soma = 0

while i != 0:
    i = int(input())
    par = i % 2
    impar = i % 2

    if par == 0:
        spar += i
    
    elif impar != 0: 
        simpar += i
    
    soma += i 
    
print(spar)
print(simpar)
print(soma)
