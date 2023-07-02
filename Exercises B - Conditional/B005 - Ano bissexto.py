ano = int(input())
resto = ano % 400
resto2 = ano % 4
resto3 = ano % 100

if ano > 0:
    if resto == 0:
        print(1)

    elif resto2 == 0 and resto3 != 0:
        print(1)

    else:
        print(0)

else:
    print(-1)
