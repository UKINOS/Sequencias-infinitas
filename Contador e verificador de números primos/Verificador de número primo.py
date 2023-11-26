def primo(elprimo):
    for n in range(2,(elprimo + 1)):
        if (elprimo % n == 0):
            if (elprimo != n):
                return "Não é primo"
            else:
                return "É primo"

while True:
    repetidor = True
    while repetidor == True:
        elprimo = input("Insira o número que você quer verificar se é primo: ")
        if elprimo.isdigit():
            elprimo = int(elprimo)
            repetidor = False
        else:print("Por favor, insira um número *positivo* (sem espaços)\n\n\n")
    resultado = primo(elprimo)
    if resultado == None:
        resultado = "Não é primo"
    print("%s\n\n\n"%resultado)