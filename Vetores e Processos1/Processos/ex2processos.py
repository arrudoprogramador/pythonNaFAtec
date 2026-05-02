import platform
import subprocess


def os():
    return platform.system()


def executa_processo(opcao, valor=None):
    nome_os = os()

    if nome_os == 'Windows':
        if opcao == 1:
            vetor_proc = ['tasklist']
        elif opcao == 2:
            vetor_proc = ['taskkill', '/PID', str(valor), '/F']
        elif opcao == 3:
            vetor_proc = ['taskkill', '/IM', str(valor), '/F']

    elif nome_os == 'Linux':
        if opcao == 1:
            vetor_proc = ['ps', 'aux']
        elif opcao == 2:
            vetor_proc = ['kill', '-9', str(valor)]
        elif opcao == 3:
            vetor_proc = ['pkill', '-9', str(valor)]

    else:
        print('SO não suportado')
        return

    with subprocess.Popen(vetor_proc, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as proc:
        for raw_linha in proc.stdout:
            print(raw_linha.decode('cp1252' if os() == 'Windows' else 'utf-8', errors='ignore'), end='')

        for raw_err in proc.stderr:
            print(raw_err.decode('cp1252' if os() == 'Windows' else 'utf-8', errors='ignore'), end='')


def main():
    while True:
        print('\n1 - Listar processos')
        print('2 - Matar por PID')
        print('3 - Matar por nome')
        print('9 - Encerrar')

        opcao = int(input('\nEscolha uma opção: '))

        if opcao == 1:
            executa_processo(1)

        elif opcao == 2:
            pid = input('Digite o PID do processo: ')
            executa_processo(2, pid)

        elif opcao == 3:
            nome = input('Digite o nome do processo: ')
            executa_processo(3, nome)

        elif opcao == 9:
            print('Encerrando...')
            break

        else:
            print('Opção inválida')


if __name__ == '__main__':
    main()