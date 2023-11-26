import decimal 

fim = int(input("Quantas casas vc quer calcular em pi?: "))
valor = decimal.Decimal(3)
posi = 1
X = 2 

decimal.getcontext().prec = fim

while fim != 0:
    if posi == 0:
        valor -= decimal.Decimal(4) / (decimal.Decimal(X) * decimal.Decimal(X + decimal.Decimal(1)) * decimal.Decimal(X + decimal.Decimal(2)))
        posi = 1
    elif posi == 1:
        valor += decimal.Decimal(4) / (decimal.Decimal(X) * decimal.Decimal(X + decimal.Decimal(1)) * decimal.Decimal(X + decimal.Decimal(2)))
        posi = 0
    X += 2
    fim -= 1
    print(str(decimal.Decimal(valor)))

print("\n\n\n\n" + str(decimal.Decimal(valor)))

print(len(str(valor)))
input("Aperte enter para fechar o programa")