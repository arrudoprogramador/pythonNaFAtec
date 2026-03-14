## Declaracao de variaveis
notas = []
soma: float = 0.0

## Inicio
for i in range(4):
    nota = float(input(f"Digite a {i+1}° nota: "))
    notas.append(nota)
    soma += nota
    
media = soma/4

## Saida
if(media >= 6.0):
    print("Aprovado")
elif(media >= 3.0) and (media < 6.0):
    print("Exame")
elif(media<3.0):
    print("Retido")
