## Declaracao de variaveis
numA: int = 0
numB: int = 0

## Inicio
def ordenar():
    numA = int(input('Digite o primeiro valor:'))
    numB = int(input('Digite o segundo valor:'))

    if(numA < numB):
        print(numA, ",", numB)
    elif(numA > numB):
        print(numB, ",", numA)
    else:
        print(numA, ",", numB)

def main():
    ordenar()

if __name__ == "__main__":
    main()
## Fim
