from calendar import monthrange
from datetime import date, timedelta


class PeriodoInvalido(Exception):
    pass


def resolver_periodo(referencia: str, data_referencia: date | None = None) -> dict:
    hoje = data_referencia or date.today()
    referencia = referencia.strip().lower()

    if referencia == "hoje":
        inicio = fim = hoje

    elif referencia == "ontem":
        inicio = fim = hoje - timedelta(days=1)

    elif referencia == "mes_atual":
        inicio = hoje.replace(day=1)
        ultimo_dia = monthrange(hoje.year, hoje.month)[1]
        fim = hoje.replace(day=ultimo_dia)

    elif referencia == "mes_passado":
        primeiro_dia_mes_atual = hoje.replace(day=1)
        fim = primeiro_dia_mes_atual - timedelta(days=1)
        inicio = fim.replace(day=1)

    elif referencia == "ano_atual":
        inicio = hoje.replace(month=1, day=1)
        fim = hoje.replace(month=12, day=31)

    else:
        raise PeriodoInvalido(
            f"Período '{referencia}' não reconhecido. "
            "Use: hoje, ontem, mes_atual, mes_passado, ano_atual."
        )

    return {
        "data_inicio": inicio.isoformat(),
        "data_fim": fim.isoformat(),
    }