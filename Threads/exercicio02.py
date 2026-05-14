import multiprocessing
import time
import random

def processamento(id, valores):
    soma = 0

    print("Início da linha", id)

    for i in range(5):
        soma = soma + valores[i]
        time.sleep(0.2)

    print("Linha", id, "-> Soma =", soma)
    print("Fim da linha", id)

def main():
    proc = 3
    params = [(0, [])] * proc

    for i in range(proc):
        valores = [0] * 5

        for j in range(5):
            valores[j] = random.randint(1, 100)

        params[i] = (i + 1, valores)

    with multiprocessing.Pool(processes=proc) as pool:
        pool.starmap(processamento, params)

if __name__ == '__main__':
    main()