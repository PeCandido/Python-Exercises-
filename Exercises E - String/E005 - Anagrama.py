palavra1 = list(input())
palavra2 = list(input())
p1_correcao = palavra1
p2_correcao = palavra2
anagrama = 1

if " " in palavra1:
    p1_correcao = []
    i = 0
    while i < len(palavra1):
        if palavra1[i] != " ":
            p1_correcao.append(palavra1[i])
        i += 1

if " " in palavra2:
    p2_correcao = []
    i = 0
    while i < len(palavra2):
        if palavra2[i] != " ":
            p2_correcao.append(palavra2[i])
        i += 1

if len(p1_correcao) != len(p2_correcao):
    anagrama = 0

else:  
    i = 0
    cont1 = 0
    cont2 = 0
    
    while i < len(p1_correcao) and anagrama == 1:
        j = 0
        while j < len(p1_correcao):
            if p1_correcao[i] == p1_correcao[j]:
                cont1 += 1
            j += 1
        
        k = 0
        while k < len(p2_correcao):
            if p1_correcao[i] == p2_correcao[k]:
                cont2 += 1
            k += 1
        
        if cont1 == cont2:
            i += 1

        else:
            anagrama = 0

        cont1 = 0
        cont2 = 0

print(anagrama)
    