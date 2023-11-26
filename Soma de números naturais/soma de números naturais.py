input("Ao apertar enter, vc vai entrar em um loop infinito que pode travar o pc se deixar muito tempo rodando...")

with open("Soma de naturais.txt", "w") as a:
    a.write("Esses são os números naturais:\n")
numeronatural = 0
somasfeitas = 0 

while True:
    numeronatural += somasfeitas
    somasfeitas += 1
    print(str(numeronatural))
    with open("soma de naturais.txt", "a") as a:
        a.write(str(numeronatural) + "\n")