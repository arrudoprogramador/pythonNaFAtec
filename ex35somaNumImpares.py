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

for num in range(inicio, fim + 1):
    divisores = 0

    for i in range(1, num + 1):
        if num % i == 0:
            divisores = divisores + 1

    if divisores == 2:
        soma = soma + num

print("Soma dos números primos:", soma)
## Fim