import math

## Declaracao de variaveis
a = float
b = float
c = float
delta = float
raiz1 = float
raiz2 = float

## Inicio
print('CALCULADORA DE RAIZ QUADRADA')

a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))

delta = (b*b) - 4*a*c

## Saida
if(delta > 0):
    raiz1 = (-b + math.sqrt(delta)) / (2*a)
    raiz2 = (-b - math.sqrt(delta)) / (2*a)
    print ('\nRaiz 1 :', raiz1, '\n Raiz 2: ', raiz2)

elif(delta == 0):
    raiz1 = -b/(2*a)
    print ('As duas raizes valem:', raiz1)

elif(delta < 0):
    print('Não existem raizes reais')

