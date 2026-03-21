## Início
def entrada_valores():
    numVoltas = int(input("Digite o número de voltas:"))
    distancia = int(input("Digite a extensão do circuito em metros:"))
    tempo = int(input("Digite a duração em minutos:"))

    return(numVoltas, distancia, tempo)

def calculo_velocidade_media(numVoltas, distancia, tempo):
    velocidadeMedia = ((distancia * numVoltas) / 1000) / (tempo / 60)
    return(velocidadeMedia)

def apresentar_resultado(velocidadeMedia):
    print(f"Velocidade média: {velocidadeMedia:.2f} km/h")

def main():
    numVoltas, distancia, tempo = entrada_valores()
    velocidadeMedia = calculo_velocidade_media(numVoltas, distancia, tempo)
    apresentar_resultado(velocidadeMedia)

if __name__ == "__main__":
    main()

## Fim