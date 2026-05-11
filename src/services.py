import requests

def buscar_cotacao_dolar():
    url = "https://economia.awesomeapi.com.br/last/USD-BRL"
    # Adicionar headers ajuda a API a aceitar a conexão do servidor
    headers = {'User-Agent': 'Mozilla/5.0'} 
    
    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            dados = response.json()
            return float(dados["USDBRL"]["bid"])
        return None
    except:
        return None