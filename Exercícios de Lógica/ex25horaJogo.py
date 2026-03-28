## Declaracao de variaveis
horaInicio: int = 0
horaFinal: int = 0
minutosInicio: int = 0
minutosFinal: int = 0
horaTempoJogo: int = 0
minutoTempoJogo: int = 0

## Início
def calculoTempo():
    global horaInicio, horaFinal, minutosInicio, minutosFinal, horaTempoJogo, minutoTempoJogo

    horaInicio = int(input("Digite apenas a hora inicial (00 até 23):"))
    minutosInicio = int(input("Digite apenas a minutagem inicial (00 até 59):"))
    horaFinal = int(input("Digite apenas a hora final (00 até 23):"))
    minutosFinal = int(input("Digite apenas a minutagem final (00 até 59):"))

    if ((horaInicio > horaFinal) or (horaInicio == horaFinal and minutosInicio > minutosFinal)):
        horaTempoJogo = (24 - horaInicio) + horaFinal
    else:
        horaTempoJogo = horaFinal - horaInicio

    if (minutosInicio > minutosFinal):
        minutoTempoJogo = (60 - minutosInicio) + minutosFinal 
        horaTempoJogo -= 1
    else:
        minutoTempoJogo = minutosFinal - minutosInicio

    print("Demorou:", horaTempoJogo, "horas e ", minutoTempoJogo, "minutos")

def main():
    calculoTempo()

if __name__ == "__main__":
    main()
    
## Fim

