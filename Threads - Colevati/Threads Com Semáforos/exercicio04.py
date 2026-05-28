import threading
import random
import time

pista = threading.Semaphore(5)
equipes = {
    "Volkswagen": threading.Semaphore(1),
    "Chevrolet": threading.Semaphore(1),
    "Ford": threading.Semaphore(1),
    "Fiat": threading.Semaphore(1),
    "Toyota": threading.Semaphore(1),
    "Honda": threading.Semaphore(1),
    "Renault": threading.Semaphore(1)
}

def piloto(nome, equipe):
    with equipes[equipe]:
        with pista:

            print(f"{nome} da equipe {equipe} entrou na pista\n")
            
            for volta in range(1, 4):
                tempo_volta = round(random.uniform(1, 3), 2)
                time.sleep(tempo_volta)

                print(f"{nome} - {equipe} " f"completou volta {volta} " f"em {tempo_volta} segundos")
            print(f"\n{nome} saiu da pista\n")

carros = [
    ("Fusca Azul", "Volkswagen"),
    ("Gol Quadrado", "Volkswagen"),

    ("Chevette Tubarão", "Chevrolet"),
    ("Corsa 40cv", "Chevrolet"),

    ("DelRey Ghia", "Ford"),
    ("Ka Batido", "Ford"),

    ("Uno com Escada", "Fiat"),
    ("Palio Fire", "Fiat"),

    ("Corolla vovô", "Toyota"),
    ("Etios Nãopais", "Toyota"),

    ("Civic manco", "Honda"),
    ("Fit rosa", "Honda"),

    ("Kwid de Firma", "Renault"),
    ("Sandero quadradão", "Renault")
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