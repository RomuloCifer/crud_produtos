from database import get_connection

def inserir_produto(nome:str, preco:float, quantidade:int) -> None:
    """ Insere um novo produto na tabela produtos
    """
    #Abrindo conexão com o banco
    conn = get_connection()
    cursor = conn.cursor()

    #Novo registro
    sql = """
            INSERT INTO produtos (nome, preco, quantidade) VALUES (?, ?, ?)""" # com placeholders para evitar problemas (:
    
    cursor.execute(sql, (nome, preco, quantidade))

    conn.commit()

    conn.close()

def listar_produtos():
    """Lista todos os produtos da db"""

    conn = get_connection()
    cursor = conn.cursor()

    sql = """
            SELECT id, nome, preco, quantidade
            FROM produtos
            ORDER BY id"""
    
    cursor.execute(sql)

    produtos = cursor.fetchall()

    conn.close()

    return produtos