import os

valor: int = 0
dir = '/tmp/exercicios'
arq = 'ex34.txt'


def criar_pasta():
# Criar uma pasta com a permissão 744 (leitura, escrita e execução para o proprietário, leitura e execução para os outros)

    os.makedirs(dir, exist_ok=True)
    os.chmod(dir, 0o744)

def mult(vlr, tab):
    res = vlr * tab

    return res

def grava(i, rslt):
    global dir, arq

    caminho = os.path.join(dir, arq)
    linha = str(rslt) + '\n'

    if not os.path.exists(caminho):
        tipo = 'w'
    elif i > 0:
        tipo = 'a'
    
    with open(caminho, tipo) as f:
        f.write(linha)

def main():
    global valor
    
    criar_pasta()

    vlr = int(input(f'Digite o um valor entre 1 e 10: '))

    for i in range(1, 11):
        res = mult(i, vlr)
        grava(i, res)
    

if __name__ == "__main__":
    main()