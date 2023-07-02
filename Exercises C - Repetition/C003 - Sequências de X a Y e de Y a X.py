x = int(input())
y = int(input())
x2 = y
y2 = x

if x > y:
    print("INVALIDO")
    
while x <= y:
    print(x)
    x += 1

while x2 >= y2:
    print(x2)
    x2 -= 1