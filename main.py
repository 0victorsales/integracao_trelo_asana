from src.trello import metodos_trello
from src.asana import metodos_asana
from src.asana import api_asana
from src.trello import api_trello

#NOTE - Trello
id_workspace = "1206889103473198"
id_card_trello = "65fb534d0fd4357edff342e7"
nome_board = "Projeto teste"
board_id = "65fad02fbeee90fcbd0464fb"
nome_list = "list teste"
id_list = "65fad02f1cce5a2ab1f57d93"

#NOTE - Asana
task_gid = "1206892577938892"
workspace_gid_asana = "1206889103473198"
project_id_asana = "1206889635666466"
nome_projeto = "Projeto do victor"



#SECTION - Asana
#NOTE - Criar projeto Asana
# a = api_asana.criar_project(nome_projeto,id_workspace)
# print(a)

# #NOTE - Criar task no Asana
# dicionarios_dados_card = metodos_trello.get_dados_card(id_card_trello)
# name_task = dicionarios_dados_card["nome_card"]
# descricao_task = dicionarios_dados_card["descricao_card"]
# prazo_task = dicionarios_dados_card["data_entrega"]
# api_asana.criar_task(project_id_asana, name_task,descricao_task, prazo_task,workspace_gid_asana )

# #NOTE - Deletar task Asana
# api_asana.delete_task(task_gid)

#SECTION - Trello
# api_trello.criar_board(nome_board)

# api_trello.delete_board(board_id)

# api_trello.criar_list(nome_list, board_id)

# api_trello.arquivar_list(id_list)

#NOTE - Criar card
# dados_task = metodos_asana.get_dados_task(task_gid)
# nome_task = dados_task["nome_task"]
# descricao_task = dados_task["descricao_task"]
# data_conclusao = dados_task["data_conclusao"]
# api_trello.criar_card(id_list, nome_task, descricao_task, data_conclusao)

api_trello.delete_card(id_card_trello)

