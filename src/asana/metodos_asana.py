from src.asana import api_asana

def get_dados_task(task_gid):
    dados_task = api_asana.get_task(task_gid)
    nome_task = dados_task["name"]
    descricao_task = dados_task["notes"]
    data_conclusao = dados_task["due_at"]
    dicionario_task = {
            "nome_task":nome_task,
            "descricao_task": descricao_task,
            "data_conclusao": data_conclusao
            }
    return dicionario_task
   

