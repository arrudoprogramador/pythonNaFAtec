## Declaracao de variaveis
primAng: float = 0
segundAng: float = 0
tercAng: float = 0

## Inicio
primAng = float(input('Digite o valor do primeiro angulo:'))
segundAng = float(input('Digite o valor do segundo angulo:'))

tercAng = 180 - (primAng + segundAng)

print('O terceiro angulo e de:', tercAng)
## Fim