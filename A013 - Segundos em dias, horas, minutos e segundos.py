segundos = int(input())
dias = segundos // 86400
horas = (segundos % 86400) // 3600
minutos = (segundos % 86400) % 3600 // 60
seg = segundos % 86400 % 3600 % 60

print(dias, horas, minutos, seg)