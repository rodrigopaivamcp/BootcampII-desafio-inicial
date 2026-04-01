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
            print(f"\n Total acumulado: R$ {total:.2f}")
            for g in gastos:
                print(f" • {g['descricao']}: R$ {g['valor']:.2f}")

        elif opcao == "3":
            print("Até logo!")
            break

if __name__ == "__main__":
    main()