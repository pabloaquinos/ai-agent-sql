import json

import boto3

def obter_segredo(nome_segredo: str, region_name: str) -> dict:
    client = boto3.client("secretsmanager", region_name=region_name)
    resposta = client.get_secret_value(SecretID=nome_segredo)
    return json.loads(resposta["SecretString"])