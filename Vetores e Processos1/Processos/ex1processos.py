import platform
import subprocess


def os():
    return platform.system()


def le_ping():
    nome_os = os()

    if nome_os == 'Windows':
        vetor_proc = ['ping', '-4', '-n', '10', 'www.google.com.br']
    elif nome_os == 'Linux':
        vetor_proc = ['ping', '-4', '-c', '10', 'www.google.com.br']
    else:
        print('SO não suportado')
        return

    with subprocess.Popen(vetor_proc, stdout=subprocess.PIPE) as saida:
        for raw_linha in saida.stdout:
            linha = raw_linha.decode('cp1252', errors='ignore')

            if nome_os == 'Windows' and 'dia' in linha:
                # 'Mínimo = 5ms, Máximo = 5ms, Média = 5ms'
                media = linha.split('=')[-1].strip()
                print('Média do ping:', media)

            elif nome_os == 'Linux' and 'min/avg/max' in linha:
                # rtt min/avg/max/mdev = 10.1/20.2/30.3/0.5 ms
                media = linha.split('=')[1].strip().split('/')[1]
                print('Média do ping:', media, 'ms')


def main():
    le_ping()


if __name__ == '__main__':
    main()