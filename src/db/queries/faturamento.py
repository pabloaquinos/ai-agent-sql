from src.db.query_guard import executar_query

SQL_FATURAMENTO = """
WITH faturamento_filtrado AS (
    SELECT
        cd_vendedor,
        nm_familia,
        dt_dia,
        nu_vol_liq,
        nu_rob,
        fl_cliente_coberto
    FROM vendas
    WHERE dt_dia BETWEEN :data_inicio AND :data_fim
      AND (:codigo_vendedor IS NULL OR cd_vendedor = :codigo_vendedor)
      AND (:familia IS NULL OR nm_familia = :familia)
)
SELECT
    COALESCE(SUM(nu_rob), 0) AS total_faturado,
    COALESCE(SUM(nu_vol_liq), 0) AS total_volume,
    COUNT(*) FILTER (WHERE fl_cliente_coberto) AS clientes_cobertos,
    COUNT(*) AS total_registros
FROM faturamento_filtrado
"""


def obter_faturamento(
    data_inicio: str,
    data_fim: str,
    codigo_vendedor: str | None = None,
    familia: str | None = None,
) -> dict:
    parametros = {
        "data_inicio": data_inicio,
        "data_fim": data_fim,
        "codigo_vendedor": codigo_vendedor,
        "familia": familia,
    }
    resultado = executar_query(SQL_FATURAMENTO, parametros=parametros)
    return resultado[0]