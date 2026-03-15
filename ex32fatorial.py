## Declaração de variáveis
num: int = 0
fatorial: int = 1

## Início

num = int(input('Digite o número a ser fatorado: '))
i = num

while i > 0:
    fatorial =+ fatorial * i
    i -= 1

print(fatorial)

## Fim