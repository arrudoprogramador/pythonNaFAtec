## Declaracao de variaveis
alturaMaria: float = 1.50
alturaAna: float = 1.10
anos: int = 0

## Inicio
while (alturaMaria > alturaAna):
    anos += 1
    alturaAna += 0.03
    alturaMaria += 0.02

print("Levará", anos, "anos para que Ana fique maior que Maria")
## Fim