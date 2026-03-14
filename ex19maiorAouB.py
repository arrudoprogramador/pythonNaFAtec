## Declaracao de variaveis
numA: int = 0
numB: int = 0
maior: int = 0

## Inicio
numA = int(input("Digite o primeiro valor:"))
numB = int(input("Digite o segundo valor:"))

if(numA > numB):
    maior = numA
elif(numB > numA):
    maior = numB
elif(numB == numA):
    maior = numA

## Saida
print("O maior número é o:", maior)