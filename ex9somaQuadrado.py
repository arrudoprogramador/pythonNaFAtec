## Declaracao de variaveis
numA: int = 0
numB: int = 0
quaNumA: int = 0
quaNumB: int = 0
soma: int = 0

## Inicio
numA = int(input('Digite o primeiro valor:'))
numB = int(input('Digite o segundo valor:'))

quaNumA = numA * numA
quaNumB = numB * numB

soma = quaNumA + quaNumB

## Saida
print('Soma dos quadrados:', soma)
