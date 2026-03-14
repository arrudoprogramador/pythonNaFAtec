## Declaracao de variaveis
numA: int = 0
numB: int = 0
diferenca: int = 0

## Inicio
numA = int(input("Digite o primeiro valor:"))
numB = int(input("Digite o segundo valor:"))

if(numA > numB):
    diferenca = numA - numB
elif(numA < numB):
    diferenca = numB - numA
elif(numA == numB):
    diferenca = 0

## Saida
print("A diferença dos números é de:", diferenca)
