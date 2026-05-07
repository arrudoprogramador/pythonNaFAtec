import math

## Declaracao de variaveis
catetoA: int = 0
catetoB: int = 0
hipotenusa: int = 0

## Inicio
catetoA = int(input('Digite o valor do cateto A:'))
catetoB = int(input('Digite o valor do cateto B:'))

hipotenusa = math.sqrt((catetoA*catetoA) + (catetoB*catetoB))

print('Valor da hipotenusa:',hipotenusa)
## Fim