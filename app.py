import streamlit as st
from src.services import buscar_cotacao_dolar

st.title("💰 Meu Controle de Gastos")

total_reais = st.number_input("Digite o valor total em R$", min_value=0.0, value=100.0)

st.write("---")


cotacao = buscar_cotacao_dolar()

if cotacao is not None:
    total_dolar = total_reais / cotacao
    
    col1, col2 = st.columns(2)
    col1.metric("Cotação Hoje", f"R$ {cotacao:.2f}")
    col2.metric("Total em Dólar", f"$ {total_dolar:.2f}")
else:
    st.error("Não conseguimos obter a cotação do dólar agora. Verifique sua conexão.")

st.write("---")
st.info("App atualizado via GitHub!")