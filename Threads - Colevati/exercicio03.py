import multiprocessing
import random
import time

def corrida(id, distancia_maxima):
    distancia = 0

    print("Sapo", id, "começou a corrida")

    while distancia < distancia_maxima:
        salto = random.randint(1, 5)
        distancia = distancia + salto

        print("Sapo", id,
              "pulou", salto, "cm",
              "| Percorreu", distancia, "cm")
        time.sleep(0.2)

    print("Sapo", id, "chegou ao final da corrida")

def main():
    proc = 5
    distancia_maxima = 50
    params = [(0, 0)] * proc

    for i in range(proc):
        params[i] = (i + 1, distancia_maxima)

    with multiprocessing.Pool(processes=proc) as pool:
        pool.starmap(corrida, params)

if __name__ == '__main__':
    main()