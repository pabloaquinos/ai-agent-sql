import jwt
from fastapi import Header, HTTPException

from src.config import settings

_jwks_url = (
    f"https://cognito-idp.{settings.aws_region}.amazonaws.com/"
    f"{settings.cognito_user_pool_id}/.well-known/jwks.json"
)

_jwks_cliente = jwt.PyJWKClient(_jwks_url)

def validar_token(authorization: str | None = Header(default=None)) -> dict:
    if authorization is None or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Token ausente ou mal formatado.")

    token = authorization.removeprefix("Bearer ").strip()

    try:
        chave_assinatura = _jwks_cliente.get_signing_key_from_jwt(token)
        payload = jwt.decode(
            token, 
            chave_assinatura.key,
            algorithms=["RS256"],
            audience=settings.cognito_client_id,
            issuer=(
                f"https://cognito-idp.{settings.aws_region}.amazonaws.com/"
                f"{settings.cognito_user_pool_id}"
            ),
        )
    except jwt.PyJWTError as erro:
        raise HTTPException(status_code=401, detail=f"Token invalido: {erro}")

    return payload
