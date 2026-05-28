import threading
import random
import time

# Apenas 2 aviões podem circular na área
area_decolagem = threading.Semaphore(2)

# Apenas 1 avião por pista
pista_norte = threading.Semaphore(1)
pista_sul = threading.Semaphore(1)


def aviao(id_aviao):

    print(f"Avião {id_aviao} aguardando entrada na área\n")

    # Controle da área de circulação
    with area_decolagem:

        print(f"Avião {id_aviao} entrou na área de decolagem\n")

        # Escolha aleatória da pista
        pista_escolhida = random.choice(["Norte", "Sul"])

        if pista_escolhida == "Norte":
            pista = pista_norte
        else:
            pista = pista_sul

        # Controle da pista
        with pista:

            print(f"Avião {id_aviao} ocupou a pista {pista_escolhida}\n")

            # MANOBRA
            tempo_manobra = round(random.uniform(0.3, 0.7), 2)
            print(f"Avião {id_aviao} manobrando "
                  f"({tempo_manobra}s)")
            time.sleep(tempo_manobra)

            # TAXIAMENTO
            tempo_taxi = round(random.uniform(0.5, 1.0), 2)
            print(f"Avião {id_aviao} taxiando "
                  f"({tempo_taxi}s)")
            time.sleep(tempo_taxi)

            # DECOLAGEM
            tempo_decolagem = round(random.uniform(0.6, 0.8), 2)
            print(f"Avião {id_aviao} decolando "
                  f"({tempo_decolagem}s)")
            time.sleep(tempo_decolagem)

            # AFASTAMENTO
            tempo_afastamento = round(random.uniform(0.3, 0.8), 2)
            print(f"Avião {id_aviao} afastando da área "
                  f"({tempo_afastamento}s)")
            time.sleep(tempo_afastamento)

            print(f"\nAvião {id_aviao} finalizou a decolagem")
            print(f"Avião {id_aviao} liberou a pista "
                  f"{pista_escolhida}\n")


threads = []

# Criação dos 12 aviões
for i in range(1, 13):

    t = threading.Thread(
        target=aviao,
        args=(i,)
    )

    threads.append(t)

# Inicia as threads
for t in threads:
    t.start()

# Aguarda finalização
for t in threads:
    t.join()

print("Todas as decolagens foram concluídas!")