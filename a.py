import asana
from asana.rest import ApiException
from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv()

# Substitua '<YOUR_ACCESS_TOKEN>' pelo seu token de acesso pessoal
access_token = os.getenv('TOKEN_ASANA')

configuration = asana.Configuration()
configuration.access_token = access_token
api_client = asana.ApiClient(configuration)

# create an instance of the API class
workspaces_api_instance = asana.WorkspacesApi(api_client)
opts = {
    'limit': 50, # int | Results per page. The number of objects to return per page. The value must be between 1 and 100.
    # 'offset': "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9", # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
    'opt_fields': "email_domains,is_organization,name,offset,path,uri", # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get multiple workspaces
    api_response = workspaces_api_instance.get_workspaces(opts)
    for data in api_response:
        pprint(data)
except ApiException as e:
    print("Exception when calling WorkspacesApi->get_workspaces: %s\n" % e)


