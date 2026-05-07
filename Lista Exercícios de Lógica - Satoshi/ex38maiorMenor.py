import os

num = [0] * 10
dir = 'Lista Exercícios de Lógica - Satoshi/temp/exercicios'
arq = 'ex38.txt'

def criar_pasta():
    os.makedirs(dir, exist_ok=True)
    os.chmod(dir, 0o744)

def receber_numeros():
    
    for i in range(10):
        num[i] = int(input(f"Digite o {i+1} número:"))

    numMaior = num[0]
    numMenor = num[0]

    return numMenor, numMaior


def verifica_maior_menor(numMenor, numMaior, num):
    for i in range(10):
        if(num[i] > numMaior):
            numMaior = num[i]
        if(num[i] < numMenor):
            numMenor = num[i]
    
    return numMenor, numMaior


def apresenta_valor(numMenor, numMaior):
    print("Menor número:", numMenor, "\n"
            "Maior número:", numMaior)

    
def gravar_em_arquivo(numMenor,numMaior):
    global dir, arq

    caminho = os.path.join(dir, arq)
    
    if not os.path.exists(caminho):
        tipo = 'w'
    else:
        tipo = 'a'

    with open(caminho, tipo) as f:
        f.write(f"Menor numero: {numMenor}\n")
        f.write(f"Maior numero: {numMaior}\n")


def main():
    criar_pasta()
    numMenor, numMaior = receber_numeros()
    numMenor, numMaior = verifica_maior_menor(numMenor, numMaior, num)
    gravar_em_arquivo(numMenor, numMaior)
    apresenta_valor(numMenor, numMaior)

if __name__ == '__main__':
    main()