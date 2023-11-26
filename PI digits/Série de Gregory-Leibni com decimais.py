import decimal

fim = int(input("Quantas casas vc quer calcular em pi?: "))
valor = decimal.Decimal(0)
posi = 1
a = 1

decimal.getcontext().prec = fim

while fim != 0:
    if posi == 0:
        valor -= decimal.Decimal(4) / decimal.Decimal(a)
        posi = 1
    elif posi == 1:
        valor += decimal.Decimal(4) / decimal.Decimal(a)
        posi = 0
    a += 2
    fim -= 1
    print(str(decimal.Decimal(valor)))

print("\n\n\n\n" + str(decimal.Decimal(valor)))

print(len(str(valor)))
input("Aperte enter para fechar o programa")