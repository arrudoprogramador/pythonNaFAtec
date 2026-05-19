import threading
import random
import time

pista = threading.Semaphore(5)
equipes = {
    "Volkswagen": threading.Lock(),
    "Chevrolet": threading.Lock(),
    "Ford": threading.Lock(),
    "Fiat": threading.Lock(),
    "Toyota": threading.Lock(),
    "Honda": threading.Lock(),
    "Renault": threading.Lock()
}

def piloto(nome, equipe):
    lock_equipe = equipes[equipe]
    lock_equipe.acquire()
    pista.acquire()

    try:
        print(f"{nome} da equipe {equipe} entrou na pista\n")
        for volta in range(1, 4):
            tempo_volta = round(random.uniform(1, 3), 2)
            time.sleep(tempo_volta)

            print(f"{nome} - {equipe} " f"completou volta {volta} " f"em {tempo_volta} segundos")
        print(f"\n{nome} saiu da pista\n")

    finally:
        pista.release()
        lock_equipe.release()

carros = [
    ("Fusca Azul", "Volkswagen"),
    ("Gol Quadrado", "Volkswagen"),

    ("Chevette Tubarão", "Chevrolet"),
    ("Corsa 40cv", "Chevrolet"),

    ("DelRey Ghia", "Ford"),
    ("Ka Batido", "Ford"),

    ("Uno com Escada", "Fiat"),
    ("Palio Fire", "Fiat"),

    ("Corolla Brad Pitt", "Toyota"),
    ("Etios Indestrutível", "Toyota"),

    ("Civic Rebaixado", "Honda"),
    ("Fit Surpreendente", "Honda"),

    ("Kwid de Firma", "Renault"),
    ("Sandero RS", "Renault")
]

threads = []

for nome, equipe in carros:
    t = threading.Thread(
        target=piloto,
        args=(nome, equipe)
    )

    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

print("Treino encerrado!")