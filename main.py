from src.trello import metodos_trello
from src.asana import metodos_asana
from src.asana import api_asana


id_workspace = "1206889103473198"
id_card_trello = "65fad030e459d83df2a6a74c"
nome_projeto = "Projeto do victor"

a = api_asana.criar_project(nome_projeto,id_workspace)
print(a)

#NOTE - Criar task no Asana
dicionarios_dados_card = metodos_trello.get_dados_card(id_card_trello)
nome_card = dicionarios_dados_card["nome_card"]
descricao_card = dicionarios_dados_card["descricao_card"]
data_entrega = dicionarios_dados_card["data_entrega"]

metodos_asana.criar_task_asana(nome_card, descricao_card,data_entrega)

