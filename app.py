import streamlit as st
import requests


@st.cache_data(ttl=3600)
def buscar_cotacao_dolar_direto():
    try:
        url = "https://economia.awesomeapi.com.br/last/USD-BRL"
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            dados = response.json()
            return float(dados["USDBRL"]["bid"])
        
        # Se der erro 429, vamos retornar um valor padrão ou None
        return None
    except:
        return None
st.title(" Controle de Gastos (Versão Única)")

valor_reais = st.number_input("Valor em R$", min_value=0.0, value=0.0)

cotacao = buscar_cotacao_dolar_direto()

if cotacao is None:
    cotacao = 5.15 
    st.warning(" Nota: Caso a A API de cotação esteja instável, usando valor padrão de R$ 5,15.")
else:
    st.success(f" Cotação obtida: R$ {cotacao:.2f}")

if valor_reais > 0:
    valor_dolar = valor_reais / cotacao
    st.metric("Total em Dólar", f"US$ {valor_dolar:.2f}")