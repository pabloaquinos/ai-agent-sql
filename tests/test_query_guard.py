from src.db.query_guard import executar_query


def test_executar_query_aceita_select_simples():
    resultado = executar_query("SELECT 1 AS valor")
    assert resultado[0]["valor"] == 1


def test_executar_query_aceita_cte():
    resultado = executar_query("WITH x AS (SELECT 1 AS valor) SELECT * FROM x")
    assert resultado[0]["valor"] == 1