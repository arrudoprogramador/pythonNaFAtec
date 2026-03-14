## Declaracao de variaveis
numA: int = 0
numB: int = 0

## Inicio
numA = int(input('Digite o primeiro valor:'))
numB = int(input('Digite o segundo valor:'))

## Saida
if(numA < numB):
    print(numA, ",", numB)
elif(numA > numB):
    print(numB, ",", numA)
else:
    print(numA, ",", numB)

