fim = int(input("Quantas casas vc quer calcular em pi?: "))
valor = (3)
posi = 1
X = 2 

while fim != 0:
    if posi == 0:
        valor -= (4) / ((X) * (X + (1)) * (X + (2)))
        posi = 1
    elif posi == 1:
        valor += (4) / ((X) * (X + (1)) * (X + (2)))
        posi = 0
    X += 2
    fim -= 1
    print(str((valor)))

print("\n\n\n\n" + str((valor)))

print(len(str(valor)))
input("Aperte enter para fechar o programa")