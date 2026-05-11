import requests

def buscar_cotacao_dolar():
    url = "https://economia.awesomeapi.com.br/last/USD-BRL"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            dados = response.json()
            return float(dados["USDBRL"]["bid"])
        
        return None
    except Exception as e:
        print(f"Erro de conexão: {e}")
        return None