import multiprocessing
import time
import random

pos_cheg: int = 0
pos_saida: int = 0
semaforo = None

def init(cheg, sai, s):
    global pos_cheg
    global pos_saida
    global semaforo
    pos_cheg = cheg
    pos_saida = sai 
    semaforo = s

def carro(id):
    global semaforo
    
    carro_andando(id)
    #início seção crítica
    with semaforo:
        carro_parado(id)
    #fim seção crítica
    carro_saindo(id)

def carro_andando(id):
    global pos_cheg

    dist: int = 0
    dist_total: int = 0
    desloc:int = 0
    tempo: float = 0.0

    desloc = 100
    tempo = 0.1
    dist_total = random.randint(1000, 2000)
    while (dist <= dist_total):
        dist += desloc  #dist = dist + desloc
        time.sleep(tempo)
        print('Carro #',id,'percorreu',dist,'m.')
    pos_cheg.value += 1
    print('Carro #',id,'foi o',pos_cheg.value,'o. a chegar')

def carro_parado(id):
    global pos_saida
    tempo_parado: float = 0.0

    print('Carro #',id,'estacionou')
    tempo_parado = random.randint(1000, 3000)
    tempo_parado = tempo_parado / 1000  
    time.sleep(tempo_parado)

    pos_saida.value += 1
    print('Carro #',id,'foi o',pos_saida.value,'o. a sair')  

def carro_saindo(id):
    print('Carro #',id,'deixou o estacionamento')

def main():
    j: int = 0
    params: int = [0]*10
    chegada: int = 0
    saida: int = 0
    sem = None

    chegada = multiprocessing.Value('i', 0)
    saida = multiprocessing.Value('i', 0)

    for j in range(10):
        params[j] = j

    with multiprocessing.Manager() as manager:
        sem = manager.Semaphore(3)
        with multiprocessing.Pool(processes=10, initializer=init, initargs=(chegada, saida, sem)) as pool:
            pool.map(carro, params)

if __name__ == '__main__':
    main()