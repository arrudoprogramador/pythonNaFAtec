## Inicio
def entrada_valores():
    numA = int(input("Digite o primeiro valor:"))
    numB = int(input("Digite o segundo valor:"))

    return numA, numB

def diferenca_valores(numA, numB):
    if(numA > numB):
        diferenca = numA - numB
    elif(numA < numB):
        diferenca = numB - numA
    elif(numA == numB):
        diferenca = 0

    return diferenca

def apresentar_diferenca(diferenca):
    print("A diferença dos números é de:", diferenca)

def main():
    numA, numB = entrada_valores()
    diferenca = diferenca_valores(numA, numB)
    apresentar_diferenca(diferenca)

if __name__ == "__main__":
    main()
## Fim
