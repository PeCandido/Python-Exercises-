n = int(input())

soma = 0
i = 1
while i <= n:
    if n % i == 0 and i != n:
        soma += i
    
    i += 1

if soma == n:
    print("S")

else:
    print("N")   
