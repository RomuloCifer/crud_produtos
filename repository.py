from database import get_connection
from produto import Produto

def inserir_produto(produto: Produto) -> Produto:
    """ Insere um novo produto e retorna com ID preenchido.
    """
    #Abrindo conexão com o banco
    conn = get_connection()
    cursor = conn.cursor()
    #Novo registro
    sql = """
            INSERT INTO produtos (nome, preco, quantidade) VALUES (?, ?, ?)""" # com placeholders para evitar problemas (:
    
    cursor.execute(sql, (produto.nome, produto.preco, produto.quantidade))

    conn.commit()
    produto_id = cursor.lastrowid # pega o ID gerado pelo proprio banco.
    conn.close()
    produto.id = produto_id
    return produto

def listar_produtos() -> list[Produto]:
    """Lista todos os produtos da db"""

    conn = get_connection()
    cursor = conn.cursor()

    sql = """
            SELECT id, nome, preco, quantidade
            FROM produtos
            ORDER BY id"""
    cursor.execute(sql)
    linhas = cursor.fetchall()
    conn.close()
    produtos = [
        Produto(id=linha[0], nome=linha[1], preco=linha[2], quantidade=linha[3])
        for linha in linhas
    ]
    return produtos


def atualizar_produto(produto: Produto) -> bool:
    """Atualiza um produto já existente"""
    if produto.id is None:
        return False # Sem ID
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
        UPDATE produtos SET nome = ?, preco = ?, quantidade = ?
        WHERE id = ?
        """
    cursor.execute(sql, (produto.nome, produto.preco, produto.quantidade, produto.id))
    conn.commit()
    linhas_afetadas = cursor.rowcount # quantas linhas foram alteradas
    conn.close()
    return linhas_afetadas > 0

def deletar_produto(produto_id:int) -> bool:
    """Deleta um produto de acordo com o ID fornecido"""
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
        DELETE FROM produtos
        WHERE id = ?
        """
    cursor.execute(sql, (produto_id,))
    conn.commit()
    linhas_removidas = cursor.rowcount
    conn.close()
    return linhas_removidas > 0