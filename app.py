import streamlit as st
import requests

def buscar_cotacao_dolar_direto():
    try:
        url = "https://economia.awesomeapi.com.br/last/USD-BRL"
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            dados = response.json()
            return float(dados["USDBRL"]["bid"])
        return None
    except Exception as e:
        print(f"Erro detalhado: {e}")
        return None

st.title("💰 Controle de Gastos (Versão Única)")

valor_reais = st.number_input("Valor em R$", min_value=0.0, value=0.0)

cotacao = buscar_cotacao_dolar_direto()

if cotacao is not None:
    valor_dolar = valor_reais / cotacao
    st.metric("Cotação", f"R$ {cotacao:.2f}")
    st.metric("Total em Dólar", f"US$ {valor_dolar:.2f}")
else:
    st.error("Erro ao carregar cotação.")