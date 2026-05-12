import streamlit as st
try:
    from src.services import buscar_cotacao_dolar
except ImportError:
    st.error("Erro: Não foi possível encontrar 'src/services.py'. Verifique a estrutura das pastas.")

st.set_page_config(page_title="Controle de Gastos", page_icon="💰")
st.title("💰 Meu Controle de Gastos")

total_reais = st.number_input("Digite o valor total das despesas (R$):", min_value=0.0, value=0.0, step=10.0)

st.write("---")


cotacao = None 

try:
    cotacao = buscar_cotacao_dolar()
except Exception as e:
    st.error(f"Erro ao processar cotação: {e}")

if cotacao is not None and cotacao > 0:
    total_dolar = total_reais / cotacao
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric(label="Cotação USD/BRL Hoje", value=f"R$ {cotacao:.2f}")
    
    with col2:
        st.metric(label="Total em Dólar", value=f"US$ {total_dolar:.2f}")
        
    st.success(f"Conversão realizada com sucesso!")
else:
    st.warning("A cotação do dólar não está disponível no momento. Verifique sua conexão ou a API.")
    st.info("O cálculo em dólar aparecerá assim que a cotação for carregada.")

st.write("---")
st.caption("Desenvolvido para o Desafio Bootcamp II")