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
projects_api_instance = asana.ProjectsApi(api_client)
project_gid = "1206890793067999" # str | Globally unique identifier for the project.


try:
    # Delete a project
    api_response = projects_api_instance.delete_project(project_gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->delete_project: %s\n" % e)