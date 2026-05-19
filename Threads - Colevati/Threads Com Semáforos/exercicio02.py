import threading
import time
import random

# Semáforo da porta
porta = threading.Semaphore(1)

def pessoa(nome):

    velocidade = random.randint(4, 6)

    distancia = 200

    tempo_corredor = distancia / velocidade

    print(f"{nome} está andando no corredor")
    print(f"{nome} velocidade: {velocidade} m/s")
    print(f"{nome} levará {tempo_corredor:.2f} segundos para chegar\n")

    time.sleep(tempo_corredor)

    print(f"{nome} chegou na porta e está esperando")

    porta.acquire()

    try:

        print(f"{nome} está atravessando a porta")

        tempo_porta = random.randint(1, 2)

        time.sleep(tempo_porta)

        print(f"{nome} atravessou a porta em {tempo_porta} segundos\n")

    finally:

        porta.release()


# Criando threads
p1 = threading.Thread(target=pessoa, args=("Pessoa 1",))
p2 = threading.Thread(target=pessoa, args=("Pessoa 2",))
p3 = threading.Thread(target=pessoa, args=("Pessoa 3",))
p4 = threading.Thread(target=pessoa, args=("Pessoa 4",))

# Iniciando threads
p1.start()
p2.start()
p3.start()
p4.start()

# Espera todas terminarem
p1.join()
p2.join()
p3.join()
p4.join()

print("Todas as pessoas atravessaram a porta.")