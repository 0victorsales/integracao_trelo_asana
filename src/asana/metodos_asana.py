from src.asana import api_asana

def get_dados_task(task_gid):
    """
        Retorna os dados de uma task do Asana com base em seu GID.

        Parâmetros:
                task_gid (str): O GID da tarefa no Asana.

        Retorna:
                dict: Um dicionário contendo o nome da tarefa, a descrição e a data de conclusão, se disponíveis.

        

        Exemplo:
                get_dados_task('1206889635666466')
                {'nome_task': 'integração', 'descricao_task': '', 'data_conclusao': None}
    """
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
   
def get_dados_projeto(project_gid):
    """
        Retorna o nome de um projeto do Asana com base em seu GID.

        Parâmetros:
                project_gid (str): O GID do projeto no Asana.

        Retorna:
                str: O nome do projeto.

        

        Exemplo:
                get_dados_projeto('1206889635666466')
                'integração'
    """
    
    dados_projeto = api_asana.get_project(project_gid)
    nome_projeto = dados_projeto["name"]
    return nome_projeto


