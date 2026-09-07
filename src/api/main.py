from fastapi import Depends, FastAPI
from pydantic import BaseModel

from src.agent.agent import criar_agente
from src.agent.memoria import criar_gerenciador_memoria
from src.observability.tracing import iniciar_langfuse
from src.api.auth import validar_token

app = FastAPI(title="Agente SQL IA")
iniciar_langfuse()

class PerguntaRequest(BaseModel):
    pergunta: str
    session_id: str

class PerguntaResponse(BaseModel):
    resposta: str

@app.get("/health")
def health() -> dict:
    return {"status": "ok"}

@app.post("/perguntar", response_model=PerguntaResponse)
def perguntar(
        requisicao: PerguntaRequest,
        payload_token: dict = Depends(validar_token),
) -> PerguntaResponse:
    actor_id = payload_token["sub"]

    with criar_gerenciador_memoria(
        actor_id=actor_id,
        session_id=requisicao.session_id,
    ) as gerenciador:
        agente = criar_agente(session_manager=gerenciador)
        resultado = agente(requisicao.pergunta)
        return PerguntaResponse(resposta=str(resultado))