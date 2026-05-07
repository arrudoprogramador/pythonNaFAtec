## Vou integrar uma API para busca de data em tempo real. http://worldtimeapi.org/api/timezone/America/Sao_Paulo/
from datetime import datetime

def receber_valores():
    diaNascimento = int(input("Digite o dia em que você nasceu:"))
    mesNascimento = int(input("Digite o mês em que você nasceu:"))
    anoNascimento = int(input("Digite o ano em que você nasceu:"))

    diaAtual = int(input("Digite o dia atual:"))
    mesAtual = int(input("Digite o mês atual:"))
    anoAtual = int(input("Digite o ano atual:"))

    return diaNascimento, mesNascimento, anoNascimento, diaAtual, mesAtual, anoAtual

def calcular_idade(diaNascimento, mesNascimento, anoNascimento, diaAtual, mesAtual, anoAtual):
    if(mesAtual < mesNascimento):
        idadeAno = (anoAtual - anoNascimento) - 1
        idadeMes = (mesAtual + 12) - mesNascimento
    else:
        idadeAno = (anoAtual - anoNascimento)
        idadeMes = mesAtual - mesNascimento
        
    idadeDia = (diaAtual - diaNascimento)

    return idadeAno, idadeMes, idadeDia

def apresentar_resultado(idadeAno, idadeMes, idadeDia):
    print("Você tem:", idadeAno, "ano(s)," , idadeMes, "mês(es) e", idadeDia, "dias")

def main():
    diaNascimento, mesNascimento, anoNascimento, diaAtual, mesAtual, anoAtual = receber_valores()
    idadeAno, idadeMes, idadeDia = calcular_idade(diaNascimento, mesNascimento, anoNascimento, diaAtual, mesAtual, anoAtual)
    apresentar_resultado(idadeAno, idadeMes, idadeDia)


if __name__ == "__main__":
    main()