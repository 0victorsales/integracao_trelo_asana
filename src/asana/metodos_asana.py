import api_asana

def criar_task_asana(project_id_asana,name_task,descricao_task,prazo_task ):
    project_id_asana = project_id_asana
    name_task = name_task
    descricao_task = descricao_task
    prazo_task = prazo_task    
    api_asana.criar_task(project_id_asana, name_task,descricao_task, prazo_task)
   

criar_task_asana()