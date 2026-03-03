## Declaracao de variaveis
litrosGast = float
tempPercur = float
velocidMedia = float
distancia = float
consumo = 12.0

## Inicio
litrosGast = float(input('Digite quantos litros foram gastos:'))
tempPercur = float(input('Digite quanto tempo demorou:'))

distancia = litrosGast * consumo
velocidMedia = distancia/tempPercur

## Saida
print('Foi percorrido ', distancia, 'kilometros, com uma velocidade media de', velocidMedia, 'km/h')
