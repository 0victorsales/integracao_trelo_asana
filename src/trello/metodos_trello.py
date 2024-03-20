# import api_trello 
from src.trello import api_trello


def get_dados_card(id_card):
    """
    Responsavel por obter dados do card do trelo
    parametro:
        -id do card trello
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
id_card_trello = "65fad030e459d83df2a6a74c"
a = get_dados_card(id_card_trello)
print(a)



