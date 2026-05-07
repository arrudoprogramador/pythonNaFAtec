## Declaracao de variaveis
valorFinal: float = 0
valorDeposito: float = 0

# Inicio
valorDeposito = float(input('Digite o valor depositado:'))
valorFinal = valorDeposito + ((valorDeposito * 1.3) / 100)

print(valorFinal)
## Fim
