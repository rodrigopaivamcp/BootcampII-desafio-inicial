import streamlit as st
import requests

# 1. Configuracao Inicial
st.set_page_config(page_title="Gestor de Gastos", layout="wide")

# Inicializa a lista de gastos na sessao se ela nao existir
if 'lista_gastos' not in st.session_state:
    st.session_state.lista_gastos = []

# 2. Funcao de Cotacao com Cache
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

# --- TOPO DO APP ---
st.title("Gestor de Gastos Multitens")

cotacao = buscar_cotacao()
if cotacao is None:
    cotacao = 5.15
    st.warning("Caso a API esteja instavel, usando valor fixo de R$ 5,15 para os calculos.")
else:
    st.success(f"Cotacao obtida em tempo real: R$ {cotacao:.2f}")

# --- FORMULARIO DE ENTRADA ---
with st.container(border=True):
    st.subheader("Adicionar Novo Gasto")
    col1, col2, col3 = st.columns([3, 2, 1])
    
    with col1:
        novo_item = st.text_input("Item/Produto", placeholder="Ex: Tenis, Almoco, Curso...")
    with col2:
        novo_valor = st.number_input("Valor em Reais (R$)", min_value=0.0, step=1.0)
    with col3:
        st.write("") 
        st.write("") 
        botao_adicionar = st.button("Adicionar", use_container_width=True)

# Logica para inserir na lista
if botao_adicionar:
    if novo_item and novo_valor > 0:
        st.session_state.lista_gastos.append({
            "item": novo_item,
            "valor_rs": novo_valor,
            "valor_us": novo_valor / cotacao
        })
        st.rerun() 
    else:
        st.error("Por favor, preencha o nome e um valor maior que zero.")

# --- EXIBICAO DA LISTA ---
if st.session_state.lista_gastos:
    st.divider()
    st.subheader("Itens Lancados")
    
    # Variavel para controlar a remocao fora do loop
    indice_para_remover = None

    # Cabecalho da Tabela
    h1, h2, h3, h4 = st.columns([3, 2, 2, 1])
    h1.write("**Item**")
    h2.write("**Valor (R$)**")
    h3.write("**Valor (US$)**")
    h4.write("**Acao**")

    # Linhas da Tabela
    for i, gasto in enumerate(st.session_state.lista_gastos):
        c1, c2, c3, c4 = st.columns([3, 2, 2, 1])
        c1.write(gasto['item'])
        c2.write(f"R$ {gasto['valor_rs']:.2f}")
        c3.write(f"US$ {gasto['valor_us']:.2f}")
        
        # Botao de excluir com chave unica
        if c4.button("Remover", key=f"btn_{i}"):
            indice_para_remover = i

    # Executa a remocao se o botao foi clicado
    if indice_para_remover is not None:
        st.session_state.lista_gastos.pop(indice_para_remover)
        st.rerun()

    # --- RESUMO TOTAL ---
    st.divider()
    total_rs = sum(item['valor_rs'] for item in st.session_state.lista_gastos)
    total_us = sum(item['valor_us'] for item in st.session_state.lista_gastos)

    t1, t2 = st.columns(2)
    t1.metric("TOTAL EM REAIS", f"R$ {total_rs:.2f}")
    t2.metric("TOTAL EM DOLAR", f"US$ {total_us:.2f}")

    if st.button("Limpar Lista Completa"):
        st.session_state.lista_gastos = []
        st.rerun()
else:
    st.info("Sua lista esta vazia. Adicione itens acima.")