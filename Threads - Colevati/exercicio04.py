import threading
import subprocess
import platform


def ping(nome, servidor):

    sistema = platform.system()

    if sistema == "Windows":
        comando = ["ping", "-4", "-n", "10", servidor]

    elif sistema == "Linux":
        comando = ["ping", "-4", "-c", "10", servidor]

    else:
        print("Sistema Operacional não suportado")
        return

    processo = subprocess.Popen(
        comando,
        stdout=subprocess.PIPE,
        text=True
    )

    soma = 0
    qtd = 0

    for linha in processo.stdout:

        if "time=" in linha or "tempo=" in linha:

            if "time=" in linha:
                tempo = linha.split("time=")[1].split()[0]

            else:
                tempo = linha.split("tempo=")[1].split()[0]

            valor = ""

            for c in tempo:
                if c.isdigit():
                    valor += c

            if valor != "":
                soma += int(valor)
                qtd += 1

            print(nome, "->", tempo)

    if qtd > 0:
        media = soma / qtd
        print(nome, "-> Tempo médio =", media, "ms")


def main():

    t1 = threading.Thread(
        target=ping,
        args=("UOL", "www.uol.com.br")
    )

    t2 = threading.Thread(
        target=ping,
        args=("Terra", "www.terra.com.br")
    )

    t3 = threading.Thread(
        target=ping,
        args=("Google", "www.google.com.br")
    )

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()


if __name__ == "__main__":
    main()