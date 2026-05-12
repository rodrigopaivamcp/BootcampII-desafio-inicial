import streamlit as st
import requests

# Configuração da página (opcional, deixa o app mais bonito)
st.set_page_config(page_title="Controle de Gastos")

@st.cache_data(ttl=3600)  # Guarda a cotação por 1 hora para evitar erro 429
def buscar_cotacao_dolar_direto():
    try:
        url = "https://economia.awesomeapi.com.br/last/USD-BRL"
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            dados = response.json()
            return float(dados["USDBRL"]["bid"])
        
        return None  # Retorna None se a API der erro (ex: 429)
    except Exception:
        return None

# --- INTERFACE DO APP ---

st.title(" Controle de Gastos (Versão Final)")
st.markdown("Converta seus gastos de Reais para Dólares de forma simples.")

# 1. Entrada do Nome do Produto
item_nome = st.text_input("O que você comprou?", placeholder="Ex: Monitor, Assinatura de Software, Jantar...")

# 2. Entrada do Valor em Reais
valor_reais = st.number_input("Valor pago em Reais (R$)", min_value=0.0, step=0.01)

st.divider() # Linha separadora visual

# 3. Lógica de Cotação e Cálculo
if valor_reais > 0:
    cotacao = buscar_cotacao_dolar_direto()
    
    # Verifica se a API funcionou ou se usamos o Fallback
    if cotacao is None:
        cotacao = 5.15 
        st.warning(" Caso a API esteja instável, usando valor fixo de R$ 5,15 para o cálculo.")
    else:
        st.success(f" Cotação obtida em tempo real: R$ {cotacao:.2f}")
    
    # Cálculo final
    valor_dolar = valor_reais / cotacao
    
    # Exibição dos Resultados
    if item_nome:
        st.subheader(f"Resumo do Gasto: {item_nome}")
    else:
        st.subheader("Resumo do Gasto")
        
    col1, col2 = st.columns(2)
    col1.metric("Valor em R$", f"R$ {valor_reais:.2f}")
    col2.metric("Total em Dólar", f"US$ {valor_dolar:.2f}")

else:
    st.info("Digite um valor acima de zero para ver a conversão.")

# Rodapé informativo
st.caption("Dados de cotação fornecidos por AwesomeAPI / Yahoo Finance.")