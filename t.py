import asana
from asana.rest import ApiException
from pprint import pprint

from dotenv import load_dotenv
import os
import json

access_token = os.getenv('TOKEN_ASANA')

configuration = asana.Configuration()
configuration.access_token = access_token
api_client = asana.ApiClient(configuration)

# create an instance of the API class
tasks_api_instance = asana.TasksApi(api_client)
task_gid = "1206891335169286" 


try:
    # Delete a task
    api_response = tasks_api_instance.delete_task(task_gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->delete_task: %s\n" % e)