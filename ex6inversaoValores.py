## Declaracao de variaveis
x: int = 0
y: int = 0
z: int = 0


## Inicio
x = int(input('Digite o valor de X:'))
y = int(input('Digite o valor de Y:'))

z = x
x = y
y = z

## Saida
print('Valor de X:', x, '\nValor de Y:', y)