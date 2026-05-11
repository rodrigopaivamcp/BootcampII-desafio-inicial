import streamlit as st
from src.core import adicionar_gasto, calcular_total
from src.services import buscar_cotacao_dolar

st.title("💰 Gerenciador de Gastos Pro")

# Inicializa a lista de gastos na memória do navegador
if "gastos" not in st.session_state:
    st.session_state.gastos = []

# Interface de entrada
nome = st.text_input("O que você comprou?")
valor = st.number_input("Quanto custou?", min_value=0.0)

if st.button("Adicionar Gasto"):
    st.session_state.gastos = adicionar_gasto(st.session_state.gastos, nome, valor)
    st.success("Gasto adicionado!")

# Exibição dos resultados
if st.session_state.gastos:
    st.subheader("Seus Lançamentos")
    for g in st.session_state.gastos:
        st.write(f"- {g['nome']}: R$ {g['valor']:.2f}")
    
    total = calcular_total(st.session_state.gastos)
    st.divider()
    st.metric("Total em Reais", f"R$ {total:.2f}")
    
    # Integração com a API
    cotacao = buscar_cotacao_dolar()
    if cotacao:
        st.metric("Total em Dólar", f"US$ {total/cotacao:.2f}", help=f"Cotação: {cotacao}")