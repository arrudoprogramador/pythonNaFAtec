import os

dir = 'temp/exercicios'
arq_entrada = 'ex38.txt'
arq_saida = 'part2_ex38.txt'


def leitura():
    caminho = os.path.join(dir, arq_entrada)
    numeros = []

    if not os.path.exists(caminho):
        print("Arquivo não encontrado!")
        return []

    with open(caminho, 'r', encoding='latin-1') as f:
        for linha in f:
            linha = linha.strip().lower()

            # pega o número depois dos dois pontos
            if "menor" in linha or "maior" in linha:
                try:
                    numero = int(linha.split(":")[1].strip())
                    numeros.append(numero)
                except:
                    continue

    return numeros


def verificar_multiplos(numeros):
    return [n for n in numeros if n % 5 == 0]


def escrever(numeros):
    os.makedirs(dir, exist_ok=True)

    caminho = os.path.join(dir, arq_saida)

    with open(caminho, 'w') as f:
        for n in numeros:
            f.write(f"{n}\n")

    print("Arquivo gerado com sucesso!")


def main():
    nums = leitura()
    multiplos = verificar_multiplos(nums)
    print("Múltiplos de 5:", multiplos)
    escrever(multiplos)


if __name__ == '__main__':
    main()