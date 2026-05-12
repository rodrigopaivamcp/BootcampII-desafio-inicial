import streamlit as st
import requests

# Configuração da página
st.set_page_config(page_title="Gestor de Gastos em Dólar", layout="wide")

# 1. Inicialização do "Banco de Dados" temporário (Session State)
if 'lista_gastos' not in st.session_state:
    st.session_state.lista_gastos = []

@st.cache_data(ttl=3600)
def buscar_cotacao():
    try:
        url = "https://economia.awesomeapi.com.br/last/USD-BRL"
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            return float(response.json()["USDBRL"]["bid"])
        return None
    except:
        return None

# --- TÍTULO E COTAÇÃO ---
st.title(" Gestor de Gastos Multitens")

cotacao = buscar_cotacao()
if cotacao is None:
    cotacao = 5.15
    st.warning(" API instável. Usando valor fixo de R$ 5,15 para os cálculos.")
else:
    st.success(f" Cotação do dia: R$ {cotacao:.2f}")

# --- FORMULÁRIO DE ENTRADA ---
with st.expander(" Adicionar Novo Gasto", expanded=True):
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        novo_item = st.text_input("Item/Produto", placeholder="Ex: Passagem, Jantar...")
    with col2:
        novo_valor = st.number_input("Valor (R$)", min_value=0.0, step=0.50)
    with col3:
        st.write(" ") # Espaçamento
        botao_adicionar = st.button("Adicionar à Lista")

# Lógica para adicionar o item à lista
if botao_adicionar:
    if novo_item and novo_valor > 0:
        # Salva o item na lista dentro da sessão
        st.session_state.lista_gastos.append({
            "item": novo_item,
            "valor_rs": novo_valor,
            "valor_us": novo_valor / cotacao
        })
        st.toast(f"'{novo_item}' adicionado!")
    else:
        st.error("Preencha o nome e o valor do item.")

# --- EXIBIÇÃO DA LISTA E TOTAIS ---
if st.session_state.lista_gastos:
    st.divider()
    st.subheader(" Itens Lançados")
    
    # Criando a tabela de exibição
    for i, gasto in enumerate(st.session_state.lista_gastos):
        c1, c2, c3, c4 = st.columns([3, 2, 2, 1])
        c1.write(f"**{gasto['item']}**")
        c2.write(f"R$ {gasto['valor_rs']:.2f}")
        c3.write(f"US$ {gasto['valor_us']:.2f}")
        if c4.button(key=f"del_{i}"):
            st.session_state.lista_gastos.pop(i)
            st.rerun()

    # --- RESUMO TOTAL ---
    st.divider()
    total_rs = sum(item['valor_rs'] for item in st.session_state.lista_gastos)
    total_us = sum(item['valor_us'] for item in st.session_state.lista_gastos)

    col_t1, col_t2 = st.columns(2)
    col_t1.metric("TOTAL EM REAIS", f"R$ {total_rs:.2f}")
    col_t2.metric("TOTAL EM DÓLAR", f"US$ {total_us:.2f}", delta_color="inverse")

    if st.button("Limpar Lista Completa"):
        st.session_state.lista_gastos = []
        st.rerun()
else:
    st.info("Sua lista está vazia. Adicione um item acima para começar.")