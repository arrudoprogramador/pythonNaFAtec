## Declaracao de variaveis
litrosGast: float = 0
tempPercur: float = 0
velocidMedia: float = 0
distancia: float = 0
consumo: float = 12.0

## Inicio
litrosGast = float(input('Digite quantos litros foram gastos:'))
tempPercur = float(input('Digite quanto tempo demorou:'))

distancia = litrosGast * consumo
velocidMedia = distancia/tempPercur

## Saida
print('Foi percorrido ', distancia, 'kilometros, com uma velocidade media de', velocidMedia, 'km/h')
