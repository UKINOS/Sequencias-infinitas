def primo(numero):
    for n in primos:
        index = primos.index(n)
        if(index != 0):
            if(numero % primos[index] == 0):
                return 0
    return 1

w = open("numeros primos.txt","w")
w.close()

def arquivo (numerose):
    w = open("numeros primos.txt","a")
    w.write(str(numerose) + "\n")
    w.close()

numero = 2
primos = [2]
print(numero)

arquivo("Números primos")
arquivo(numero)

while True:
    numero += 1
    resposta = primo(numero)
    if(resposta is 1 and numero is not 4):
        print(numero)
        primos.append(numero)
        arquivo(numero)