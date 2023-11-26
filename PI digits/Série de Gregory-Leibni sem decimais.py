fim = int(input("Quantas casas vc quer calcular em pi?: "))
valor = (0)
posi = 1
a = 1

while fim != 0:
    if posi == 0:
        valor -= (4) / (a)
        posi = 1
    elif posi == 1:
        valor += (4) / (a)
        posi = 0
    a += 2
    fim -= 1
    print(str((valor)))

print("\n\n\n\n" + str((valor)))

print(len(str(valor)))
input("Aperte enter para fechar o programa")