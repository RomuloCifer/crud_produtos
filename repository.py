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