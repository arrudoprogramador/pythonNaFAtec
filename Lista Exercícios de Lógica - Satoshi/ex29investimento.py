## Inicio
def entrada_valores():
    tipoInvestimento = int(input("Digite o tipo de investimento: \n" \
                                    "1-) Poupança\n" \
                                    "2-) renda fixa\n"))
    valorInvestimento = float(input("Digite a valor do investimento: "))

    return tipoInvestimento, valorInvestimento

def calculo_retorno(tipoInvestimento, valorInvestimento):
    if(tipoInvestimento == 1):
        retorno = valorInvestimento + ((valorInvestimento * 3)/100)

    elif(tipoInvestimento == 2):
        retorno = valorInvestimento + ((valorInvestimento * 5)/100)

    else:
        print("Valores inválidos")
        return None
    
    return retorno 

def apresentar_resultado(retorno):
    if retorno is not None:
        print("Valor após 30 dias: ", retorno)

def main():
    tipoInvestimento, valorInvestimento = entrada_valores()
    retorno = calculo_retorno(tipoInvestimento, valorInvestimento)
    apresentar_resultado(retorno)

if __name__ == "__main__":
    main()
## Fim
