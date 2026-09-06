from bedrock_agentcore.memory.integrations.strands.config import AgentCoreMemoryConfig
from bedrock_agentcore.memory.integrations.strands.session_manager import AgentCoreMemorySessionManager

from src.config import settings

def criar_gerenciador_memoria(actor_id: str, session_id: str) -> AgentCoreMemorySessionManager:
    config = AgentCoreMemoryConfig(
        memory_id=settings.agentcore_memory_id,
        actor_id=actor_id,
        session_id=session_id,
    )
    return AgentCoreMemorySessionManager(
        agentcore_memory_config=config,
        region_name=settings.aws_region,
    )