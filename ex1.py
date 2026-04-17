from contextlib import redirect_stdout

def calculo():
    for i in range(10, 151):
        quadrado = i * i
        print(f"Quadrado do número {i} = {quadrado}")

with open("saida.txt", "w", encoding="utf-8") as arquivo:
    with redirect_stdout(arquivo):
        calculo()

