import requests

api = "http://worldtimeapi.org/api/timezone/America/Sao_Paulo/"

try: 
    requisicao = requests.get(api)
    dicRequisicao = requisicao.json()

    print(dicRequisicao)

    
except requests.exceptions.RequestException as erro:
        print("Erro na requisição:", erro)