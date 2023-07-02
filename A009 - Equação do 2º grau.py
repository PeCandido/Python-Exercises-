a = int(input())
b = int(input())
c = int(input())

bhask1 = (-b + ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)
bhask2 = (-b - ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)

print(f"{bhask1:.2f}")
print(f"{bhask2:.2f}")
