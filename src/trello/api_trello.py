import requests
from dotenv import load_dotenv
import os 
load_dotenv()


id_board = "65fad02fbeee90fcbd0464fb"
id_list = "65faefe454b3961d12ef4bd1"
api_key = os.getenv('API_KEY')
token = os.getenv('TOKEN')

#SECTION - sessão Board
def get_board():
    try:
        url = f"https://api.trello.com/1/boards/{id_board}"

        headers = {
            "Accept": "application/json"
        }

        query = {
            'key': api_key,
            'token': token
        }

        response = requests.request("GET",url, headers=headers,params=query )
        return response.json()
        
    except Exception as e:
        print('Não foi possivel obter os dados do board, erro:',e)
        


def delete_board(id_board):
    try:
        url = f"https://api.trello.com/1/boards/{id_board}"

        query = {
            'key': api_key,
            'token': token
        }

        response = requests.request("DELETE", url, params=query)
        return response.json()
    except Exception as e:
        print('Não foi possivel deletar o board, erro:', e)

def criar_board(nome_board):
    try:
        url = "https://api.trello.com/1/boards/"

        query = {
            'name':nome_board,
            'key': api_key,
            'token': token
        }

        response = requests.request("POST", url, params=query)
        return response.json()
    except Exception as e:
        print('Não foi possivel criar um board, erro:', e)



#SECTION - Sessao card
def get_card(id_card):
    try:
        url = f"https://api.trello.com/1/cards/{id_card}"

        headers = {
            "Accept": "application/json"
        }

        query = {
            'key': api_key,
            'token': token
        }

        response = requests.request("GET",url,headers=headers, params=query)
        return response.json()
    except Exception as e:
        print('Não foi possivel obter dados do card, erro:', e)

def delete_card(id_card):
    try:
        url = f"https://api.trello.com/1/cards/{id_card}"

        query = {
            'key': api_key,
            'token': token
        }

        response = requests.request("DELETE", url,params=query)
        return response.json()
    except Exception as e:
        print('Não foi possivel deletar o card, erro:',e)

def criar_card(id_list,nome_card,descricao_card,prazo_task):
    try:
        url = "https://api.trello.com/1/cards"

        headers = {
            "Accept": "application/json"
        }

        query = {
            'idList': id_list,
            'key': api_key,
            'token': token,
            'name': nome_card,
            'desc': descricao_card,
            'due': prazo_task
            
        }

        response = requests.request("POST", url, headers=headers,params=query)
        return response.json()
    except Exception as e:
        print('Não foi possivel criar card, erro:', e)




#SECTION - Sessao list

def get_list():
    try:
        url = f"https://api.trello.com/1/lists/{id_list}"

        query = {
            'key': api_key,
            'token': token
        }

        response = requests.request("GET",url, params=query)
        return response.json()
    except Exception as e:
        print('Não foi possivel obter listas', e)

def arquivar_list(id_list):
    try:
        url = f"https://api.trello.com/1/lists/{id_list}/closed"

        query = {
            'key': api_key,
            'token': token,
            'value': 'true'
        }

        response = requests.request("PUT", url, params=query)
        return response.json()
    except Exception as e:
        print('Não foi possivel arquivar a lista, erro:', e)


def criar_list(nome_list,id_board ):
    try:
        url = "https://api.trello.com/1/lists"

        query = {
            'name': nome_list,
            'idBoard': id_board,
            'key': api_key,
            'token': token
        }

        response = requests.request("POST", url,params=query)
        return response.json()
    except Exception as e:
        print('Não foi criar list', e)








