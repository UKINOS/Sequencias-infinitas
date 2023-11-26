import time

#Função roubada de outro código meu :)
def numeros(x, y, z):
    resposta = input("Insira o número que quer testar:")
    while True:
        resposta2 = resposta.strip("-")
        if resposta2.isdigit() == True:
            if x <= int(resposta) <= y and z == 1:
                return int(resposta)
            elif z == 0:
                return int(resposta)
            else:
                resposta = input(f"Sua resposta tem que ser entre {x} e {y}: ")
        else:
            resposta = input(f"Sua resposta precisa ser em números naturais (sem espaços, letras, ou números inteiros): ")

input("Ao apertar enter, vc entende que esse código pode facilmente travar seu computador caso o número que esteja procurando seja alto...")

while True:
    qual = 0
    A = 0
    B = 1
    N = numeros(0,0,0)
    z = time.perf_counter()
    while True:
        if qual == 0:
            A = A + B
            qual = 1
        else:
            B = A + B
            qual = 0    
        print(".", end="")
        y = time.perf_counter()
        if A + B == N or N == 0 or N == 1:
            print("\nO seu número está na sequência de Fibonacci...\n\n\n")
            print(y - z)
            break
        elif A + B >= N:
            print("\nO seu número não está na sequência de Fibonacci...\n\n\n")
            print(y - z)
            break