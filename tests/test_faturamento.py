from src.db.queries.faturamento import obter_faturamento


def test_faturamento_sem_filtro_opcional():
    resultado = obter_faturamento(data_inicio="2025-01-01", data_fim="2025-12-31")
    assert resultado["total_faturado"] >= 0
    assert "clientes_cobertos" in resultado


def test_faturamento_filtrado_por_vendedor():
    resultado = obter_faturamento(
        data_inicio="2025-01-01", data_fim="2025-12-31", codigo_vendedor="10008919"
    )
    assert resultado["total_faturado"] > 0


def test_faturamento_filtrado_por_familia():
    resultado = obter_faturamento(
        data_inicio="2025-01-01", data_fim="2025-12-31", familia="CAFE TRAD"
    )
    assert resultado["total_faturado"] == 9250.00  # 3450 + 5800, do seed


def test_faturamento_periodo_sem_dados_retorna_zero():
    resultado = obter_faturamento(data_inicio="2099-01-01", data_fim="2099-12-31")
    assert resultado["total_faturado"] == 0
    assert resultado["total_registros"] == 0