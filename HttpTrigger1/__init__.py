import logging

from azure.storage.blob import BlobServiceClient
import azure.functions as func

storage_account_key = "sEuD6mXxwM1YtAFTkut/TjjFyKnlVXKOXtjAgK+QkXaAGv1YP1lJQw3I5uq0D3lNgBQBxo6J8rj/+AStNqwWUA=="
storage_account_name = "functionexamcloudgrb3b5"
connection_string = "DefaultEndpointsProtocol=https;AccountName=functionexamcloudgrb3b5;AccountKey=sEuD6mXxwM1YtAFTkut/TjjFyKnlVXKOXtjAgK+QkXaAGv1YP1lJQw3I5uq0D3lNgBQBxo6J8rj/+AStNqwWUA==;EndpointSuffix=core.windows.net"
container_name = "storage-file"

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    path = req.params.get('path')
    name_path = req.params.get('path_name')
    if path and name_path:
        uploadToBlobStorage(path,name_path)


def uploadToBlobStorage(file_path,file_name):
   blob_service_client = BlobServiceClient.from_connection_string(connection_string)
   blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)
   with open(file_path,"rb") as data:
      blob_client.upload_blob(data)
      print(f"Uploaded {file_name}.")