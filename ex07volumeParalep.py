## Declaracao de variaveis
comprimento: float = 0
altura: float = 0
largura: float = 0
area: float = 0

## Inicio
comprimento = float(input('Digite o valor do comprimento:'))
altura = float(input('Digite o valor da altura:'))
largura = float(input('Digite o valor da largura:'))

area = altura * comprimento * largura

print('Area do paralelepipedo:', area,'m')
## Fim
