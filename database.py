import os
import psycopg2

def obtener_conexao():
    """
    Busca a URI de conexão nas variáveis de ambiente.
    Se não encontrar (rodando local), usa a string padrão do Supabase.
    """
    uri_banco = os.getenv(
        "DATABASE_URL", 
        "postgresql://postgres.daddbcspktpbxzmifrfw:tmnt2003fla03@aws-1-us-east-2.pooler.supabase.com:5432/postgres"
    )
    return psycopg2.connect(uri_banco)

def salvar_gasto_no_banco(descricao, valor, data, moeda, valor_convertido):
    """
    Insere um novo registro de gasto diretamente na tabela do Supabase.
    """
    conn = obtener_conexao()
    cursor = conn.cursor()
    try:
        query = """
            INSERT INTO gastos (descricao, valor, data, moeda, valor_convertido)
            VALUES (%s, %s, %s, %s, %s);
        """
        cursor.execute(query, (descricao, valor, data, moeda, valor_convertido))
        conn.commit()  # Confirma a gravação no banco
        print("Dados inseridos com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar no banco: {e}")
        conn.rollback()  # Cancela a operação se der erro
        raise e
    finally:
        cursor.close()
        conn.close()