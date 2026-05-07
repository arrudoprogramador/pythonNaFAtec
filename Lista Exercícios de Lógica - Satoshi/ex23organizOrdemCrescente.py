## Declaracao de variaveis
valorA: int = 0
valorB: int = 0
valorC: int = 0
valorD: int = 0

## Inicio
def organizarOrdem():
    global valorA,valorB,valorC,valorD
    
    print("* Digite os três primeiros números em ordem crescente: ")
    valorA = int(input("Digite o primeiro valor: "))
    valorB = int(input("Digite o segundo valor: "))
    valorC = int(input("Digite o terceiro valor: "))
    valorD = int(input("Digite o quarto valor: "))

    if(valorD < valorA):
        print(valorD, ",", valorA, ",", valorB,",", valorC)
    elif(valorD < valorB):
        print(valorA, ",", valorD, ",", valorB,",", valorC)
    elif(valorD < valorC):
        print(valorA, ",", valorB,",",valorD, "," ,valorC)   
    else:
        print(valorA, ",", valorB,",", valorC , ",", valorD)

def main():
    organizarOrdem()

if __name__ == "__main__":
    main()
## Fim

