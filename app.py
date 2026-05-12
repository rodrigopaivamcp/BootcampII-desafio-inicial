import streamlit as st
import requests


@st.cache_data(ttl=3600)
def buscar_cotacao_dolar_direto():
    try:
        url = "https://economia.awesomeapi.com.br/last/USD-BRL"

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        st.write("Status:", response.status_code)

        if response.status_code == 200:
            dados = response.json()

            st.write(dados)

            return float(dados["USDBRL"]["bid"])

        else:
            st.error(f"Erro HTTP: {response.status_code}")
            return None

    except Exception as e:
        st.error(f"Erro: {e}")
        return None


st.title("Controle de Gastos")

valor_reais = st.number_input(
    "Valor em R$",
    min_value=0.0,
    value=0.0
)

cotacao = buscar_cotacao_dolar_direto()

if cotacao is None:
    cotacao = 5.15
    st.warning(
        "API instável, usando valor padrão."
    )
else:
    st.success(f"Cotação: R$ {cotacao:.2f}")

if valor_reais > 0:
    valor_dolar = valor_reais / cotacao

    st.metric(
        "Total em Dólar",
        f"US$ {valor_dolar:.2f}"
    )