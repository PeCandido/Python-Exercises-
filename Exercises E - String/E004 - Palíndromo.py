palavra = input()

i = 0
j = 1
palindromo = 1
while i < len(palavra):
    if palavra[i] == ' ':
        i += 1
        
    if palavra[-j] == ' ':
        j += 1
            
    if palavra[i] != palavra[-j]:
        palindromo = 0
        break


    i += 1
    j += 1 

print(palindromo)

