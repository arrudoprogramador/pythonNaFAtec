import math

## Declaracao de variaveis
a: float = 0
b: float = 0
c: float = 0
delta: float = 0
raiz1: float = 0
raiz2: float = 0

## Inicio
def calcularRaizes():
    global a, b, c, delta, raiz1, raiz2

    print('CALCULADORA DE RAIZ QUADRADA')

    a = float(input('Digite o valor de A: '))
    b = float(input('Digite o valor de B: '))
    c = float(input('Digite o valor de C: '))

    delta = (b*b) - 4*a*c

    if(delta > 0):
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        print ('\nRaiz 1 :', raiz1, '\nRaiz 2: ', raiz2)

    elif(delta == 0):
        raiz1 = -b/(2*a)
        print ('As duas raizes valem:', raiz1)

    elif(delta < 0):
        print('Não existem raizes reais')

def main():
    calcularRaizes()

if __name__ == "__main__":
    main()
## Fim
