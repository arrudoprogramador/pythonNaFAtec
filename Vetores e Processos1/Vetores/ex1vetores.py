numero = [0]*50
media = [0]*50

def coletar():
    for i in range(50):
        numero[i] = int(input("Digite um número:"))

def distribuir():
    contador = 0
    somaMedia = 0
    somaImpares = 0

    for i in range(50):
        # Calculando média
        if numero[i] > 9 and numero[i] < 201:
            somaMedia += numero[i]
            contador += 1

        # Soma dos números ímpares
        if numero[i] % 2 == 1:
            somaImpares += numero[i]
        
    if contador > 0:
        resposta = somaMedia/contador
        print("A média desses números é:", resposta)

    print("A soma dos números ímpares é:", somaImpares)


def main():
    coletar()
    distribuir()   

if __name__ == '__main__':
    main()