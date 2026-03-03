## Declaracao de variaveis
horasTraba = float
valorHora = float
porcDesc = float
numDep = float

# Inicio
horasTraba = float(input('Digite a quantidade de horas trabalhadas:'))
valorHora = float(input('Digite o valor recebido por horas:'))
porcDesc = float(input('Digite a porcentagem de desconto:'))
numDep = float(input('Digite o número de dependentes:'))

salarioBruto = horasTraba * valorHora
salarioLiquido = salarioBruto - porcDesc
salarioFinal = salarioLiquido + (numDep * 100)

## Saida
print("O salário final será de: R$", salarioFinal)