import requests
import json
from dotenv import load_dotenv
import os 
load_dotenv()


id_board = "65faf284bcd3f67e35adde15"
id_card = "65fad2d066a81cb167fc5f9e"
id_list = "65faefe454b3961d12ef4bd1"
api_key = os.getenv('API_KEY')
token = os.getenv('TOKEN')

#SECTION - sessão Board
def get_board():
    url = f"https://api.trello.com/1/boards/{id_board}"

    headers = {
        "Accept": "application/json"
    }

    query = {
        'key': api_key,
        'token': token
    }

    response = requests.request("GET",url, headers=headers,params=query )
    if response.status_code == 200:
        return response.json()
    else:
        print('Não foi possivel obter board')

def delete_board():
    url = f"https://api.trello.com/1/boards/{id_board}"

    query = {
        'key': api_key,
        'token': token
    }

    response = requests.request("DELETE", url, params=query)
    if response.status_code == 200:
        return response.json()
    else:
        print('Não foi possivel deletar o board')

def criar_board():
    url = "https://api.trello.com/1/boards/"

    query = {
        'name': '{name}',
        'key': api_key,
        'token': token
    }

    response = requests.request("POST", url, params=query)
    if response.status_code == 200:
        return response.json()
    else:
        print('Não foi possivel criar board')



#SECTION - Sessao card
def get_card():
    url = f"https://api.trello.com/1/cards/{id_card}"

    headers = {
        "Accept": "application/json"
    }

    query = {
        'key': api_key,
        'token': token
    }

    response = requests.request("GET",url,headers=headers, params=query)
    if response.status_code == 200:
        return response.json()
    else:
        print('Não foi possivel obter dados do card')

def delete_card():
    url = f"https://api.trello.com/1/cards/{id_card}"

    query = {
        'key': api_key,
        'token': token
    }

    response = requests.request("DELETE", url,params=query)
    if response.status_code == 200:
        return response.json()
    else:
        print('Não foi possivel deletar card')

def criar_card():
    url = "https://api.trello.com/1/cards"

    headers = {
        "Accept": "application/json"
    }

    query = {
        'idList': '65faf238b94a14f07702ef2e',
        'key': api_key,
        'token': token,
        
    }

    response = requests.request("POST", url, headers=headers,params=query)
    if response.status_code == 200:
        return response.json()
    else:
        print('Não foi possivel criar card')




#SECTION - Sessao list

def get_list():
    url = f"https://api.trello.com/1/lists/{id_list}"

    query = {
        'key': api_key,
        'token': token
    }

    response = requests.request("GET",url, params=query)
    if response.status_code == 200:
        return response.json()
    else:
        print('Não foi possivel obter lista')

def arquivar_list():
    url = f"https://api.trello.com/1/lists/{id_list}/closed"

    query = {
        'key': api_key,
        'token': token,
        'value': 'true'
    }

    response = requests.request("PUT", url, params=query)
    if response.status_code == 200:
        return response.json()
    else:
        print('Não foi possivel arquivar list')
        print(response)


def criar_list():
    url = "https://api.trello.com/1/lists"

    query = {
        'name': '{name}',
        'idBoard': '65faf238b94a14f07702ef27',
        'key': api_key,
        'token': token
    }

    response = requests.request("POST", url,params=query)
    if response.status_code == 200:
        return response.json()
    else:
        print('Não possivel criar list')








a = criar_list()
print(a)
