## Declaracao de variaveis
base: int = 0
expoente: int = 0
i: int = 0

## Inicio
base = int(input("Digite o valor da base: "))
expoente = int(input("Digite o valor do expoente: "))

for i in range(expoente):
    potencia = base ** expoente

print(potencia)

## Fim