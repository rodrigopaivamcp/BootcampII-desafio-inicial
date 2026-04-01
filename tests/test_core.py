import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
from core import adicionar_gasto, calcular_total


def test_adicionar_gasto_sucesso():
    dados = []
    adicionar_gasto(dados, "Internet", 100.0)
    assert len(dados) == 1
    assert dados[0]["descricao"] == "Internet"
    assert dados[0]["valor"] == 100.0

def test_calcular_total_gastos():
    dados = [{"valor": 50.0}, {"valor": 25.5}]
    assert calcular_total(dados) == 75.5

def test_valor_negativo_deve_falhar():
    with pytest.raises(ValueError):
        adicionar_gasto([], "Erro", -10)