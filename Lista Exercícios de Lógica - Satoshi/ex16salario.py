## Declaracao de variaveis
horasTraba: float = 0
valorHora: float = 0
porcDesc: float = 0
numDep: float = 0

# Inicio
horasTraba = float(input('Digite a quantidade de horas trabalhadas:'))
valorHora = float(input('Digite o valor recebido por horas:'))
porcDesc = float(input('Digite a porcentagem de desconto:'))
numDep = float(input('Digite o número de dependentes:'))

salarioBruto = horasTraba * valorHora
salarioLiquido = salarioBruto - porcDesc
salarioFinal = salarioLiquido + (numDep * 100)

print("O salário final será de: R$", salarioFinal)
## Fim