from src.trello import metodos_trello
from src.asana import metodos_asana
from src.asana import api_asana
from src.trello import api_trello

#NOTE - Trello
id_card_trello = "65fad030e459d83df2a6a74c"
board_id = "65fad02fbeee90fcbd0464fb"
nome_list = "list teste"
id_list = "65fad02f1cce5a2ab1f57d93"

#NOTE - Asana
task_gid = "1206892577938892"
workspace_gid_asana = "1206889103473198"
project_id_asana = "1206889635666466"
project_gid = "1206889635666466" 



#SECTION - Asana
#NOTE - Criar projeto Asana
nome_projeto = metodos_trello.get_dados_board(board_id)
retorno = api_asana.criar_project(nome_projeto,workspace_gid_asana)
print(retorno)

# #NOTE - Criar task no Asana
dicionarios_dados_card = metodos_trello.get_dados_card(id_card_trello)
name_task = dicionarios_dados_card["nome_card"]
descricao_task = dicionarios_dados_card["descricao_card"]
prazo_task = dicionarios_dados_card["data_entrega"]
api_asana.criar_task(project_id_asana, name_task,descricao_task, prazo_task,workspace_gid_asana )

# #NOTE - Deletar task e projeto Asana
api_asana.delete_task(task_gid)
api_asana.delete_project(project_gid)



#SECTION - Trello
#NOTE - Criar board trello
nome_projeto = metodos_asana.get_dados_projeto(project_gid)
api_trello.criar_board(nome_projeto)

#NOTE - Criar card
dados_task = metodos_asana.get_dados_task(task_gid)
nome_task = dados_task["nome_task"]
descricao_task = dados_task["descricao_task"]
data_conclusao = dados_task["data_conclusao"]
api_trello.criar_card(id_list, nome_task, descricao_task, data_conclusao)

#NOTE - Criar list no trello
api_trello.criar_list(nome_list, board_id)

#NOTE - deletar board, list e cart trello
api_trello.delete_board(board_id)
api_trello.arquivar_list(id_list)
api_trello.delete_card(id_card_trello)

