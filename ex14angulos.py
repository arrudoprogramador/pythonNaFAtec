## Declaracao de variaveis
primAng = float
segundAng = float
tercAng = float

## Inicio
primAng = float(input('Digite o valor do primeiro angulo:'))
segundAng = float(input('Digite o valor do segundo angulo:'))

tercAng = 180 - (primAng + segundAng)

## Saida
print('O terceiro angulo e de:', tercAng)
