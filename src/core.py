def validar_valor(valor):
    """Garantia de que o gasto seja um número positivo."""
    if not isinstance(valor, (int, float)):
        raise ValueError("O valor deve ser um número.")
    if valor <= 0:
        raise ValueError("O valor deve ser maior que zero.")
    return valor

def adicionar_gasto(lista_gastos, descricao, valor):
    """Adiciona um dicionário de gasto à lista existente."""
    valor_validado = validar_valor(valor)
    novo_gasto = {"descricao": descricao, "valor": valor_validado}
    lista_gastos.append(novo_gasto)
    return lista_gastos

def calcular_total(lista_gastos):
    """Soma todos os valores da lista."""
    return sum(gasto["valor"] for gasto in lista_gastos)