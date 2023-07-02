n = int(input())
lista = list(map(int, input().split()))

i_par = []
i_impar = []

i = 0
while i < n:
    if i % 2 == 0:
        i_par.append(lista[i])
    
    else:
        i_impar.append(lista[i])
    
    i += 1

j = 0
if len(i_par) > len(i_impar):
    while j < len(i_impar):
        print(i_impar[j],end=' ')
        print(i_par[j],end=' ')

        j += 1
    print(i_par[j])

else:
    while j < len(i_par):
        print(i_impar[j],end=' ')
        print(i_par[j],end=' ')
        
        j += 1








