import threading
import random
import time

DISTANCIA_MAXIMA = 50
SALTO_MAXIMO = 5
posicao = 1

lock = threading.Lock()

def sapo(nome):
    global posicao
    distancia_percorrida = 0

    while distancia_percorrida < DISTANCIA_MAXIMA:
        salto = random.randint(1, SALTO_MAXIMO)
        distancia_percorrida += salto

        if distancia_percorrida > DISTANCIA_MAXIMA:
            distancia_percorrida = DISTANCIA_MAXIMA

        print(f"{nome} pulou {salto} cm")
        print(f"{nome} percorreu {distancia_percorrida} cm")

        time.sleep(0.5)

    lock.acquire()

    try:
        print(f"{nome} chegou em {posicao}º lugar!\n")
        posicao += 1

    finally:
        lock.release()

s1 = threading.Thread(target=sapo, args=("Sapo 1",))
s2 = threading.Thread(target=sapo, args=("Sapo 2",))
s3 = threading.Thread(target=sapo, args=("Sapo 3",))
s4 = threading.Thread(target=sapo, args=("Sapo 4",))
s5 = threading.Thread(target=sapo, args=("Sapo 5",))

# Iniciando corrida
s1.start()
s2.start()
s3.start()
s4.start()
s5.start()

# Espera todos terminarem
s1.join()
s2.join()
s3.join()
s4.join()
s5.join()

print("Corrida encerrada!")