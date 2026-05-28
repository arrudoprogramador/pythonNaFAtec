import threading
import random
import time

# Semáforos
tocha = threading.Semaphore(1)
pedra = threading.Semaphore(1)

# Lista de portas
portas = [1, 2, 3, 4]

# Porta correta
porta_certa = random.randint(1, 4)

# Controle das portas
lock = threading.Lock()


def cavaleiro(nome):

    distancia = 0

    # Velocidade inicial
    velocidade = random.randint(2, 4)

    pegou_tocha = False
    pegou_pedra = False

    print(f"{nome} começou com velocidade {velocidade}")

    while distancia < 2000:

        time.sleep(0.05)

        distancia += velocidade

        print(f"{nome} está em {distancia} metros")

        # TOCHA
        if distancia >= 500 and pegou_tocha == False:

            if tocha.acquire(blocking=False):

                pegou_tocha = True
                velocidade += 2

                print(f"{nome} pegou a TOCHA")
                print(f"{nome} ficou com velocidade {velocidade}")

        # PEDRA
        if distancia >= 1500 and pegou_pedra == False and pegou_tocha == False:

            if pedra.acquire(blocking=False):

                pegou_pedra = True
                velocidade += 2

                print(f"{nome} pegou a PEDRA")
                print(f"{nome} ficou com velocidade {velocidade}")

    print(f"\n{nome} chegou ao final!")

    # Escolha da porta
    with lock:

        porta = random.choice(portas)
        portas.remove(porta)

    print(f"{nome} escolheu a porta {porta}")

    if porta == porta_certa:
        print(f"{nome} ESCAPOU!\n")
    else:
        print(f"{nome} foi devorado pelos monstros!\n")


threads = []

# Cria os 4 cavaleiros
for i in range(1, 5):

    t = threading.Thread(
        target=cavaleiro,
        args=(f"Cavaleiro {i}",)
    )

    threads.append(t)

# Inicia
for t in threads:
    t.start()

# Espera terminar
for t in threads:
    t.join()

print("Fim do jogo!")