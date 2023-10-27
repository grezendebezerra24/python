'''
Executar no terminal: 
pip install requests
OU
py -3.11 -m pip install requests
'''

import requests

try:
    cep = input("Digite o CEP: ")
    url = f'https://viacep.com.br/ws/{cep}/json/'

    resposta = requests.get(url)

    if resposta.status_code == 200: #ou requests.codes.ok:
        dicionario = resposta.json()

        if 'erro' in dicionario:
            print("CEP inexistente")
        else:
            print(f"Rua: {dicionario['logradouro']}")
            print(f"Complemento: {dicionario['complemento']}")
            print(f"Bairro: {dicionario['bairro']}")
            print(f"UF: {dicionario['uf']}")
            print(f"Localidade: {dicionario['localidade']}")

    elif resposta.status_code == 400:
        print("ERRO: O CEP deve ter 8 caracteres")




except ConnectionError:
    print("Error: Não foi possível acessar a API")
except Exception as mensagem:
    print(f"ERRO: {mensagem}")