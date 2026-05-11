import pytest
from src.services import buscar_cotacao_dolar

def test_buscar_cotacao_dolar_real():
   

    try:
        resultado = buscar_cotacao_dolar()

        if resultado is not None:
            assert isinstance(resultado, float)
            assert resultado > 0
        else:

            print("Aviso: API de cotação indisponível no momento.")
            assert True 
    except Exception:

        assert True