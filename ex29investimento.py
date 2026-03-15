## Declaracao de variaveis
tipoInvestimento: int = 0
valorInvestimento: float = 0
retorno: float = 0

## Inicio
tipoInvestimento = int(input("Digite o tipo de investimento: \n" \
                                "1-) Poupança\n" \
                                "2-) renda fixa\n"))
valorInvestimento = float(input("Digite a valor do investimento: "))

if(tipoInvestimento == 1):
    retorno = valorInvestimento + ((valorInvestimento * 3)/100)
elif(tipoInvestimento == 1):
    retorno = valorInvestimento + ((valorInvestimento * 5)/100)

print("Valor após 30 dias: ", retorno)

## Saída
