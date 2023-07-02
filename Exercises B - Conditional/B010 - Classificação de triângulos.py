l1 = int(input())
l2 = int(input())
l3 = int(input())

if (l1 + l2) > l3 and (l1 + l3) > l2 and (l2 + l3) > l1: 
    if l1 == l2 and l2 == l3:
        print("EQUILATERO")

    elif l1 != l2 and l1 != l3 and l2 != l3:
        print("ESCALENO")

    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("ISOSCELES")

else:
    print("INVALIDO")
