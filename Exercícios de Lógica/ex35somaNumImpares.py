## Declaracao de variaveis
numA: int = 0
numB: int = 0
soma: int = 0

## Inicio
numA = int(input("Digite o primeiro número: "))
numB = int(input("Digite o segundo número: "))

if numA < numB:
    inicio = numA
    fim = numB
else:
    inicio = numB
    fim = numA

for i in range(inicio, fim + 1):
    if i % 2 != 0:
        soma += i 

print("Soma dos números impares:", soma)
## Fim