## Declaracao de variaveis
numA: int = 0 
numB: int = 0 
maior: int = 0

## Inicio
def maiorOuMenor():
    global numA, numB, maior

    numA = int(input("Digite o primeiro valor:"))
    numB = int(input("Digite o segundo valor:"))

    if(numA > numB):
        maior = numA
    elif(numB > numA):
        maior = numB
    elif(numB == numA):
        maior = numA

    print("O maior número é o:", maior)

def main():
    maiorOuMenor()

if __name__ == "__main__":
    main()

## Fim