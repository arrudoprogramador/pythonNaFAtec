## Inicio
def entrada_valores():
    precoAtual = float(input("Digite o preço atual do produto: "))
    mediaMensal = float(input("Digite a média mensal : "))
    
    return(precoAtual, mediaMensal)

def calculo_novo_preco(precoAtual, mediaMensal):
    if (mediaMensal < 500) and (precoAtual < 30.00):
        precoNovo = precoAtual + (precoAtual * 10 /100)
    elif ((mediaMensal >= 500) and (mediaMensal < 1000)) and ((precoAtual >= 30.00) and (precoAtual < 80.00)):
        precoNovo = precoAtual + (precoAtual * 15 /100)
    elif (mediaMensal >= 1000) and (precoAtual >= 80.00):
        precoNovo = precoAtual - (precoAtual * 5 /100)
    else:
        precoNovo = precoAtual
    
    return(precoNovo)

def apresentar_resultado(precoNovo):
    print("O novo preço será de:", precoNovo)

def main():
    precoAtual, mediaMensal = entrada_valores()
    precoNovo = calculo_novo_preco(precoAtual, mediaMensal)
    apresentar_resultado(precoNovo)

if __name__ == "__main__":
    main()

## Fim
