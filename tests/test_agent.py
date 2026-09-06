from src.agent.agent import criar_agente

def test_agente_tem_as_tools_esperadas():
    agente = criar_agente()
    nomes_das_tools = {tool.tool_name for tool in agente.tool_registry.registry.values()}

    assert "resolver_periodo" in nomes_das_tools
    assert "consultar_faturamento" in nomes_das_tools

def test_agente_usa_o_model_id_configurado():
    from src.config import settings

    agente = criar_agente()
    assert agente.model.config["model_id"] == settings.bedrock_model_id