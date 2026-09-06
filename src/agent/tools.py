import json

from strands import tool

from src.db.queries.faturamento import obter_faturamento as _obter_faturamento
from src.utils.periodo import PeriodoInvalido, resolver_periodo as _resolver_periodo

@tool
def resolver_periodo(referencia: str) -> str:
    """Converte uma referência textual de período em datas concretas (início e fim).

    Use esta tool ANTES de consultar faturamento sempre que o usuário mencionar
    um período relativo em vez de datas exatas (ex: "mês atual", "mês passado",
    "esse ano", "hoje", "ontem"). Não tente calcular essas datas você mesmo.

    Args:
        referencia: um dos valores: "hoje", "ontem", "mes_atual", "mes_passado", "ano_atual".
    """
    try: 
        periodo = _resolver_periodo(referencia)
        return json.dumps({"sucesso": True, **periodo})
    except PeriodoInvalido as e:
        return json.dumps({"sucesso": False, "erro": str(e)})

@tool
def consultar_faturamento(
    data_inicio: str,
    data_fim: str,
    codigo_vendedor: str | None = None,
    familia: str | None = None,
) -> str:
    """Consulta o faturamento (valor faturado e volume vendido) no período informado.

    Use esta tool quando o usuário perguntar sobre faturamento, valor vendido,
    volume vendido, ou cobertura de clientes. Sempre obtenha data_inicio e
    data_fim primeiro (use a tool resolver_periodo se o usuário mencionar um
    período relativo como "mês atual").

    Args:
        data_inicio: data inicial do período, no formato YYYY-MM-DD.
        data_fim: data final do período, no formato YYYY-MM-DD.
        codigo_vendedor: código do vendedor, se o usuário mencionar um vendedor específico.
        familia: nome da família de produto, se o usuário mencionar uma família específica
            (ex: "CAFE TRAD", "ACHOCOLATADO", "REFRESCO", "CAPSULA").
    """
    
    resultado = _obter_faturamento(
        data_inicio=data_inicio,
        data_fim=data_fim,
        codigo_vendedor=codigo_vendedor, 
        familia=familia,
    )
    return json.dumps(resultado, default=str)