n = int(input())

milhar = n // 1000
centena = (n % 1000) // 100
dezena = (n % 1000) % 100 // 10
unidade = (n % 1000) % 100 % 10

uni_invertida = unidade * 1000
dez_invertida = dezena * 100
cen_invertida = centena * 10

invertido = uni_invertida + dez_invertida + cen_invertida + milhar


print(invertido)