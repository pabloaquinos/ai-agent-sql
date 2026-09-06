from strands import Agent
from strands.models import BedrockModel

from src.agent.tools import consultar_faturamento, resolver_periodo
from src.config import settings

SYSTEM_PROMPT = """\
Você é um assistente de dados que responde perguntas sobre faturamento de vendas.

Regras obrigatórias:
1. Se o usuário mencionar um período relativo (ex: "mês atual", "mês passado",
   "esse ano", "hoje", "ontem"), use a tool resolver_periodo ANTES de consultar
   faturamento, para obter data_inicio e data_fim corretos.
2. Se o usuário já informar datas exatas, use-as diretamente, sem chamar
   resolver_periodo.
3. Use a tool consultar_faturamento para responder perguntas sobre valor
   faturado, volume vendido ou cobertura de clientes.
4. Responda sempre em português, de forma clara e objetiva, citando os
   números retornados pela tool. Nunca invente valores.
5. Se uma tool retornar erro, explique o problema ao usuário em vez de tentar
   adivinhar uma resposta.
6. Use o histórico da conversa e o que você já sabe sobre o usuário para
   entender referências como "meu vendedor preferido" ou "aquele produto".
"""

def criar_agente(session_manager: None) -> Agent:
    modelo = BedrockModel(
        model_id=settings.bedrock_model_id,
        region_name=settings.aws_region,
        temperature=0.1,
    )
    return Agent(
        model=modelo,
        system_prompt=SYSTEM_PROMPT,
        tools=[resolver_periodo, consultar_faturamento],
        session_manager=session_manager,
        callback_handler=None,
    )