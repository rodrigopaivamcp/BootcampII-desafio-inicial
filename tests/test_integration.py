import pytest
from src.services import buscar_cotacao_dolar

def test_buscar_cotacao_dolar_real():
    """
    Teste de Integração: Verifica se a função consegue se conectar 
    à API externa e retornar um valor numérico válido.
    """
    resultado = buscar_cotacao_dolar()
    
    # Verifica se a API não retornou None (falha de conexão)
    assert resultado is not None, "A API de cotação não respondeu."
    
    # Verifica se o resultado é um número (float ou int)
    assert isinstance(resultado, (float, int)), "A cotação deveria ser um número."
    
    # Verifica se o valor é positivo (não existe dólar negativo ou zero)
    assert resultado > 0, "A cotação deve ser maior que zero."

print("\n[INFO] Teste de integração concluído com sucesso!")