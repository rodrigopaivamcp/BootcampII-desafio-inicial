from services import buscar_cotacao_dolar
from core import adicionar_gasto, calcular_total

def main():
    gastos = []
    print("=== BEM-VINDO AO GESTOR DE GASTOS ===")
    
    while True:
        print("\n1. Novo Gasto | 2. Ver Total | 3. Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            desc = input("Descrição: ")
            try:
                val = float(input("Valor: R$ "))
                adicionar_gasto(gastos, desc, val)
                print("✅ Registrado!")
            except ValueError as e:
                print(f"Erro: {e}")

        elif opcao == "2":
            total = calcular_total(gastos)
            print(f"\n--- Resumo de Gastos ---")
            print(f"Total em Reais: R$ {total:.2f}")
            
           
            print("Consultando cotação do dólar...")
            cotacao = buscar_cotacao_dolar()
            
            if cotacao:
                total_usd = total / cotacao
                print(f"Total convertido: US$ {total_usd:.2f} (Cotação: {cotacao:.2f})")
            else:
                print("Não foi possível converter para dólar no momento.")
           

        elif opcao == "3":
            print("Até logo!")
            break

if __name__ == "__main__":
    main()