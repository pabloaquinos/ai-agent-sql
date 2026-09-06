from datetime import date

import pytest

from src.utils.periodo import PeriodoInvalido, resolver_periodo


def test_mes_atual():
    resultado = resolver_periodo("mes_atual", data_referencia=date(2025, 2, 15))
    assert resultado == {"data_inicio": "2025-02-01", "data_fim": "2025-02-28"}


def test_mes_atual_ano_bissexto():
    resultado = resolver_periodo("mes_atual", data_referencia=date(2024, 2, 10))
    assert resultado == {"data_inicio": "2024-02-01", "data_fim": "2024-02-29"}


def test_mes_passado_com_virada_de_ano():
    resultado = resolver_periodo("mes_passado", data_referencia=date(2025, 1, 15))
    assert resultado == {"data_inicio": "2024-12-01", "data_fim": "2024-12-31"}


def test_ano_atual():
    resultado = resolver_periodo("ano_atual", data_referencia=date(2025, 6, 1))
    assert resultado == {"data_inicio": "2025-01-01", "data_fim": "2025-12-31"}


def test_periodo_invalido_lanca_excecao():
    with pytest.raises(PeriodoInvalido):
        resolver_periodo("trimestre_atual", data_referencia=date(2025, 6, 1))