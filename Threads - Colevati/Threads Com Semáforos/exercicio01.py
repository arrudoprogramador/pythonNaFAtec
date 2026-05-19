import threading
import time
import random

semaforo = threading.Semaphore(1)

sentido_atual = ""

def carro(nome, sentido):
    global sentido_atual

    semaforo.acquire()

    try:
        sentido_atual = sentido

        print(f"{nome} está passando no sentido: {sentido_atual}")

        time.sleep(random.randint(1, 3))

        print(f"{nome} saiu do cruzamento")

    finally:
        semaforo.release()

# Criando as threads
t1 = threading.Thread(
    target=carro,
    args=("Carro 1", "Norte -> Sul")
)

t2 = threading.Thread(
    target=carro,
    args=("Carro 2", "Sul -> Norte")
)

t3 = threading.Thread(
    target=carro,
    args=("Carro 3", "Leste -> Oeste")
)

t4 = threading.Thread(
    target=carro,
    args=("Carro 4", "Oeste -> Leste")
)

# Iniciando as threads
t1.start()
t2.start()
t3.start()
t4.start()

# Espera todas terminarem
t1.join()
t2.join()
t3.join()
t4.join()

print("Todos os carros passaram.")