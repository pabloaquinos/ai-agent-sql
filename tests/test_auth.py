from unittest.mock import MagicMock, patch

import jwt
import pytest
from fastapi import HTTPException

from src.api.auth import validar_token


def test_validar_token_sem_header_lanca_401():
    with pytest.raises(HTTPException) as excecao:
        validar_token(authorization=None)
    assert excecao.value.status_code == 401


def test_validar_token_sem_prefixo_bearer_lanca_401():
    with pytest.raises(HTTPException) as excecao:
        validar_token(authorization="token-sem-bearer")
    assert excecao.value.status_code == 401


def test_validar_token_assinatura_invalida_lanca_401():
    with patch("src.api.auth._jwks_cliente.get_signing_key_from_jwt") as get_chave_simulada:
        chave_falsa = MagicMock()
        chave_falsa.key = "chave-que-nao-bate-com-a-assinatura"
        get_chave_simulada.return_value = chave_falsa

        token_qualquer = jwt.encode({"sub": "usuario-teste"}, "outra-chave", algorithm="HS256")

        with pytest.raises(HTTPException) as excecao:
            validar_token(authorization=f"Bearer {token_qualquer}")

        assert excecao.value.status_code == 401