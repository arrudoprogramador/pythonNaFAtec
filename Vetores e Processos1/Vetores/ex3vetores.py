numero = [0]*5
media = 0.0

def coletar():
    for i in range(5):
        numero[i] = int(input("Digite um número:"))

def calcular_media():
    soma = 0
    contador = 0
    global media

    for i in range(5):
        soma += numero[i]
        contador += 1

    media = soma/contador
    print("A média é:", media)
    
def abaixo_acima_media():
    acimaMedia = 0
    abaixoMedia = []

    for i in range(5):
        # Acima
        if numero[i] > media:
            acimaMedia += 1

        # Abaixo
        if numero[i] < media:

            ## função para atribuir apenas os índices .append(i)
            abaixoMedia.append(i)
            
    print("Quantidade de notas acima da média:", acimaMedia, "\nOs índices das notas abaixo da média são, respectivamente:", abaixoMedia)

def main():
    coletar()
    calcular_media()
    abaixo_acima_media()   

if __name__ == '__main__':
    main()