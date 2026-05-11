import requests

def buscar_cotacao_dolar():
    url = "https://economia.awesomeapi.com.br/last/USD-BRL"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        
        if response.status_code == 200:
            dados = response.json()
            return float(dados["USDBRL"]["bid"])
        
        print(f"Erro na API: Status {response.status_code}")
        return None
    except Exception as e:
        print(f"Falha na requisição: {e}")
        return None