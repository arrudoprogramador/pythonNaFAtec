## Declaracao de variaveis
num1: int = 0
num2: int = 0

## Início

def multiplo():
    global num1, num2
    num1 = int(input("Digite o primeiro valor inteiro: "))
    num2 = int(input("Digite o segundo valor inteiro: "))

    if(num1 > num2):
        if(num1 % num2 == 0):
            print(num1, "é múltiplo de", num2)
        else:
            print(num1, "NÃO é múltiplo de", num2)
    elif(num2 > num1):
        if(num2 % num1 == 0):
            print(num2, "é múltiplo de", num1)
        else:
            print(num2, "NÃO é múltiplo de", num1)

def main():
    multiplo()

if __name__ == "__main__":
    main()
## Fim