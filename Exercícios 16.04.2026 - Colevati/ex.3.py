import os

ARQUIVO = os.path.join("Exercícios 16.04.2026", "temp", "saida.txt")

# Função: verifica se é ímpar
def verifica_impar(num):
    if num % 2 != 0:
        return num
    return -1


# Procedimento: leitura do arquivo e impressão
def ler_arquivo_fibonacci():
    if not os.path.exists(ARQUIVO):
        print(f"Arquivo '{ARQUIVO}' não encontrado.")
        return

    with open(ARQUIVO, "r") as f:
        for linha in f:
            linha = linha.strip()

            if linha == "":
                continue

            # tenta converter para inteiro
            try:
                num = int(linha)
            except ValueError:
                # ignora linhas inválidas
                continue

            resultado = verifica_impar(num)

            if resultado != -1:
                print(resultado)


# Programa principal
ler_arquivo_fibonacci()