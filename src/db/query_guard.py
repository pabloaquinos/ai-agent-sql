from sqlalchemy import text

from src.db.connection import engine


def executar_query(sql: str, parametros: dict | None = None, limite_linhas: int = 200) -> list[dict]:
    sql_tratado = sql.strip().rstrip(";")

    if "limit" not in sql_tratado.lower():
        sql_tratado = f"{sql_tratado} LIMIT {limite_linhas}"

    with engine.connect() as conn:
        resultado = conn.execute(text(sql_tratado), parametros or {})
        colunas = resultado.keys()
        return [dict(zip(colunas, linha)) for linha in resultado.fetchall()]