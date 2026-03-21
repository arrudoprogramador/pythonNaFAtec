## Declaracao de variaveis
valor: int = 0

## Início
def divisivel():
    valor = int(input("Digite um valor inteiro:"))

    if(valor != 0) and (valor != 1):
        if(valor % 2 == 0) and (valor % 3 == 0):
            print("Valor divisível por 2 e 3")
        elif(valor % 2 == 0):
            print("Valor divisível por 2")
        elif(valor % 3 == 0):
            print("Valor divisível por 3")
    else:
        print("Valor NÃO divisível por 2 e 3")

def main():
    divisivel()

if __name__ == "__main__":
    main()
## Fim
