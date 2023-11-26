import math

def is_fibonacci(n):
    phi = 0.5 + 0.5 * math.sqrt(5.0)
    a = phi * n
    return n == 0 or abs(round(a) - a) < 1.0 / n

while True:
    try:
        num = int(input("Insira o número que deseja verificar: "))
        if is_fibonacci(num):
            print(f"{num} está na sequência de Fibonacci.")
        else:
            print(f"{num} não está na sequência de Fibonacci.")
    except:None