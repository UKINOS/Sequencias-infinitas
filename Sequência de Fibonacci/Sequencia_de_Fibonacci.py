qual = 0
A = 0
B = 1

input("Ao apertar enter, vc entende que esse código é infinito e pode facilmente travar seu computador!!")
print("0\n1")

with open("Sequência de Fibonacci.txt", "w") as f:
    f.write("Essa é a sequência de Fibonacci:\n\n0\n1\n1")

while True:
    if qual == 0:
        A = A + B
        qual = 1
        print(A)
    else:
        B = A + B
        qual = 0
        print(B)

    with open("Sequência de Fibonacci.txt", "a") as f:
        f.write("\n"+str(A + B))