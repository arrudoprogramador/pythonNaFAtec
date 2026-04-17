import os

def processo(numVezes):
    a, b = 0, 1
    for _ in range(numVezes):
        print(a)
        a, b = b, a + b

def main():
    pasta = "temp"
    arquivo = "saida.txt"

    if not os.path.exists(pasta):
        os.makedirs(pasta)

    caminho = os.path.join(pasta, arquivo)

    n = int(input("Digite n: "))

    with open(caminho, "w", encoding="utf-8") as f:
        a, b = 0, 1
        for _ in range(n):
            f.write(str(a) + "\n")
            a, b = b, a + b

    print(f"Resultados salvos em: {caminho}")

if __name__ == "__main__":
    main()
