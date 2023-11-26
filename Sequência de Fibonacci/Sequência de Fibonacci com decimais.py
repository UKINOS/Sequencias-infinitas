import decimal
qual = 0
A = decimal.Decimal(0)
B = decimal.Decimal(1)

input("Ao apertar enter, vc entende que esse código é infinito e pode facilmente travar seu computador!!")
print("0\n1")

with open("Sequência de Fibonacci.txt", "w") as f:
    f.write("Essa é a sequência de Fibonacci:\n\n0\n1\n1")

while True:
    if qual == 0:
        A = decimal.Decimal(A) + decimal.Decimal(B)
        qual = 1
        print(decimal.Decimal(A))
    else:
        B = decimal.Decimal(A) + decimal.Decimal(B)
        qual = 0
        print(decimal.Decimal(B))

    with open("Sequência de Fibonacci.txt", "a") as f:
        f.write("\n"+str(decimal.Decimal(A) + B))