## Declaracao de variaveis
kgAlimento: float = 0
duracao: float = 0

## Inicio
kgAlimento = float(input('Digite os kg do alimento:'))
duracao = kgAlimento/0.05

## Saida
print('Esse alimento vai durar:', duracao, 'dias')