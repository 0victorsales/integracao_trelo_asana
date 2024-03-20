from src.trello import api_trello


def get_dados_card(id_card):
    """
    Responsavel por obter dados do card do trelo
    Parâmetros:
        -id_card (str): O id do card trello
    return
        -dicionarios contendo nome do card, descricao e data de entrega da task
    """
    
    dados_card = api_trello.get_card(id_card)
    nome_card = dados_card["name"]
    descricao_card = dados_card["desc"]
    data_entrega = dados_card["due"]

    dic_dados = {
        "nome_card":nome_card,
        "descricao_card": descricao_card,
        "data_entrega": data_entrega
    }
    return dic_dados

def get_dados_board(id_board):
    """
    Retorna o nome de um board do Trello com base em seu ID.

    Parâmetros:
        id_board (str): O ID do board no Trello.

    Retorna:
        str: O nome do board.

 

    Exemplo:
        get_dados_board('65fad02fbeee90fcbd0464fb')
        
    """
    dados_board = api_trello.get_board(id_board)
    nome_board = dados_board["name"]
    return nome_board





