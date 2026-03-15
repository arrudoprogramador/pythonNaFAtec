## Declaração de variáveis
num: int = 0
soma: int = 0

## Início
num = int(input('Digite um número: '))

for i in range(1, num + 1):
    soma += 1 / i

print("Série:", soma)
## Fim