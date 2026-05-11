import requests # Biblioteca para fazer requisições HTTP

def buscar_cotacao_dolar():
    """
    Consome a AwesomeAPI para obter a cotação atual do Dólar (USD) em Reais (BRL).
    Este é o ponto de integração com o serviço externo.
    """
    url = "https://economia.awesomeapi.com.br/last/USD-BRL"
    
    try:
        # Realiza a chamada GET para a API
        response = requests.get(url, timeout=5)
        
        # Verifica se a conexão foi bem-sucedida (Status 200)
        if response.status_code == 200:
            dados = response.json()
            # Extrai o valor de compra (bid) da estrutura da API
            cotacao = float(dados["USDBRL"]["bid"])
            return cotacao
        
        return None # Caso a API responda algo diferente de 200
        
    except Exception as e:
        # Se houver erro de conexão (ex: sem internet), o programa não trava
        print(f"Erro ao consultar API: {e}")
        return None