import os
import psycopg2

def obter_conexao():
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
    conn = obter_conexao()
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
        
def listar_gastos_do_banco():
    """
    [ALUNO B] Busca todos os gastos salvos na tabela do Supabase.
    Retorna uma lista de tuplas com as colunas na ordem correta.
    """
    conn = obter_conexao()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT id, descricao, valor, data, moeda, valor_convertido
            FROM gastos
            ORDER BY id DESC;
        """)

        return cursor.fetchall()

    except Exception as e:
        print(f"Erro ao listar gastos: {e}")
        return []

    finally:
        cursor.close()
        conn.close()


def deletar_gasto_do_banco(gasto_id):
    """
    [ALUNO B] Remove um gasto específico da tabela utilizando o ID único.
    """
    conn = obter_conexao()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "DELETE FROM gastos WHERE id = %s;",
            (gasto_id,)
        )

        conn.commit()
        print(f"Gasto ID {gasto_id} deletado com sucesso!")

    except Exception as e:
        print(f"Erro ao deletar: {e}")
        conn.rollback()

    finally:
        cursor.close()
        conn.close()