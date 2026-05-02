import platform
import subprocess

def prop_os():
    system: str = ''
    release: str = ''
    version: str = ''
    arch: str = ''

    system = platform.system()
    release = platform.release()
    version = platform.version()
    arch = platform.architecture()

    print(system, release, version, arch)

def os():
    system: str = ''
    system = platform.system()

    return system

def proc(processo):
    vetor_proc: str = []
    vetor_proc = processo.split(' ')
    print(vetor_proc)
    subprocess.run(vetor_proc)

def le_processo(processo):
    vetor_proc: str = []
    saida: str = ''
    linha: str = ''
    vet_linha: str = []
    vet_linha2: str = []

    vetor_proc = processo.split(' ')
    print(vetor_proc)
    saida = subprocess.Popen(vetor_proc, stdout=subprocess.PIPE)
    linha = saida.stdout.readline().decode('utf-8', errors = 'ignore')

    while (linha != ''):
        # print(linha)
        if ('NAME' in linha):
            vet_linha = linha.split('                  ')
            vet_linha2 = vet_linha[1].split(' ')
            print(vet_linha2[0])
        linha = saida.stdout.readline().decode('utf-8', errors='ignore')


def main(): 
    processo: str = ''
    # prop_os()

    nome_os: str = ''
    nome_os = os()

    # #print(os_name)

    # if os_name == 'Windows':
    #     print("Fechadão com o Windows")

    # if os_name == 'Linux':
    #     print("Aqui é Linux, sem mais")

    processo = input('Digite um app: ')
    if ('ps' in processo and nome_os == 'Linux'):
        # proc(processo)
        le_processo(processo)
    else:
        if ('ps' in processo):
            print('Esse processo é do Linux')

    if ('TASKLIST' in processo and nome_os == 'Windows'):
        # proc(processo)
        le_processo(processo)
    else:
        if ('TASKLIST' in processo):
            print('Esse processo é do Windows')

if __name__ == '__main__':
    main()