## Declaracao de variaveis
anoAtual: int = 0
anoNasc: int = 0
idadeFutura: int = 0
idade: int = 0

## Inicio
anoNasc = int(input('Digite o ano de seu nascimento:'))
anoAtual = int(input('Digite o ano atual:'))

idade = anoAtual - anoNasc
idadeFutura = idade + 17

## Saida
print('Sua idade atual:', idade,'anos\nSua idade daqui 17 anos:', idadeFutura, 'anos')