import math

## Declaracao de variaveis
catetoA = int
catetoB = int
hipotenusa = int

## Inicio
catetoA = int(input('Digite o valor do cateto A:'))
catetoB = int(input('Digite o valor do cateto B:'))

hipotenusa = math.sqrt((catetoA*catetoA) + (catetoB*catetoB))

## Saida
print('Valor da hipotenusa:',hipotenusa)