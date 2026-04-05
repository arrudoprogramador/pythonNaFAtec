import os

dir = 'temp/exercicios'
arq = 'serie.txt'

def fatorial(n):
    fat = 1
    for i in range(1, n + 1):
        fat *= i
    return fat


def termo(n):
    return 1 / fatorial(n)

def calcular_serie(N):
    soma = 1 
    termos = [1]  

    for i in range(1, N + 1):
        t = termo(i)
        termos.append(t)
        soma += t

    return termos, soma

def gravar_arquivo(termos, soma):
    os.makedirs(dir, exist_ok=True)
    caminho = os.path.join(dir, arq)

    with open(caminho, 'w') as f:
        for i, t in enumerate(termos):
            if i == 0:
                f.write("1\n")
            else:
                f.write(f"1/{i}! = {t}\n")

        f.write(f"\nSoma final = {soma}\n")

    print("Arquivo gerado com sucesso!")

N = int(input("Digite N: "))

termos, soma = calcular_serie(N)
print("Resultado:", soma)

gravar_arquivo(termos, soma)