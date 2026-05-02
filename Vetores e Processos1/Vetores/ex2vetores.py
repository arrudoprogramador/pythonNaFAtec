numero = [0]*100

def coletar():
    for i in range(100):
        numero[i] = int(input("Digite um número:"))

def maior_menor_valor():
    maiorValor = numero[0]
    menorValor = numero[0]

    for i in range(100):
        # Maior
        if numero[i] > maiorValor:
            maiorValor = numero[i]

        # Menor
        elif numero[i] < menorValor:
            menorValor = numero[i]
        
    
    print("O maior número é o:", maiorValor, "\nO menor valor é o:", menorValor)

def media():
    soma = 0
    contador = 0
    media = 0

    for i in range(100):
        soma += numero[i]
        contador += 1
    
    media = soma/contador
    print("A média é:", media)

def main():
    coletar()
    maior_menor_valor()
    media()   

if __name__ == '__main__':
    main()