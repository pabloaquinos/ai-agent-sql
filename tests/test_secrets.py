from unittest.mock import MagicMock, patch

from src.aws.secrets import obter_segredo

def test_obter_segredo_retorna_dict_do_secret_string():
    resposta_simulada = {"SecretString": '{"db_user": "teste", "db_password": "1234"}'}

    cliente_simulado = MagicMock()
    cliente_simulado.get_secret_value.return_value = resposta_simulada

    with patch("boto3.client", return_value=cliente_simulado):
        resultado = obter_segredo("qualquer-segredo", region_name="us-east-1")

    assert resultado == {"db_user": "teste", "db_password": "1234"}