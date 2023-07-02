n = int(input())
palindromo = "S"
inverso = 0
reversor = n

i = 0
while reversor > 0:
    final = reversor % 10
    inverso = (inverso * 10) + final
    reversor = reversor // 10

if n != inverso:
    palindromo = "N"

print(palindromo)