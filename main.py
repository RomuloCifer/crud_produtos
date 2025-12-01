from database import create_table
from repository import inserir_produto, listar_produtos, atualizar_produto, deletar_produto
from logger import Logger

logger = Logger('produtos.log')

def ler_float(mensagem: str) -> float:
    """Lê um número float do usuário, tratando erros de entrada"""
    while True:
        valor_str = input(mensagem)
        valor_str = valor_str.replace(",", ".")  # Substitui vírgula por ponto
        try:
            valor_float = float(valor_str)

            return valor_float
        except ValueError:
            print("Valor inválido. Por favor, digite um número válido.")

def ler_int(mensagem: str) -> int:  
    """Lê um número inteiro, tratndo erros."""
    while True:
        valor_str = input(mensagem)
        valor_str = valor_str.replace(",", ".")
        try:
            valor_int = int(valor_str)
            return valor_int
        except ValueError:
            print("Valor inválido. Por favor, digite um número inteiro válido.")

def cadastrar_produto():
    """Cadastra um novo produto no sistema"""
    nome = input("Digite o nome do produto: ")
    #Usando as funções para garantir valores corretos.
    preco = ler_float("Digite o preço do produto: ")
    qtd = ler_int("Digite a quantidade do produto: ")

    inserir_produto(nome, preco, qtd)
    print("\n",nome, "cadastrado com sucesso")
    logger.create(f"Produto criado: nome={nome}, preco={preco}, quantidade={qtd}")

def mostrar_produtos():
    produtos = listar_produtos()
    if not produtos:
        print("Lista de produtos vazia.")
    else:
        for prod in produtos:
            prod_id, prod_nome, prod_preco, prod_qtd = prod
            print(f"ID:{prod_id} -> nome : {prod_nome} | preço : {prod_preco:.2f} | Quantidade : {prod_qtd}")

def atualizar_produtos():
    mostrar_produtos()

    produto_id = ler_int("ID: ")
    print("Digite os novos dados. \n")
    novo_nome = input("Nome: ")
    preco = ler_float("Preço: ")
    quantidade = ler_int("Quantidade: ")

    sucesso = atualizar_produto(produto_id, novo_nome, preco, quantidade)
    if sucesso:
        print("Item atualizado com sucesso!")
        logger.update(f"Produto ID={produto_id} atualizado para: nome={novo_nome}, preco={preco}, quantidade={quantidade}")
    else:
        print("Nenhum produto atualizado, cheque o ID")
        logger.error(f"Tentativa de atualizar produto falhou ID={produto_id}")

def deletar_produtos_flow():
    print("\n=== Excluir produto ===")
    mostrar_produtos()

    produto_id = ler_int("ID: ")
    confirmacao = input(f"Tem certeza que deseja deletar o produto ID {produto_id}? s/n")
    if confirmacao.lower() != "s":
        print("Operação cancelada..")
        return
    sucesso = deletar_produto(produto_id)
    if sucesso:
        print("Produto deletado com sucesso")
        logger.delete(f"Produto deletado ID={produto_id}")
    else:
        print("Nenhum item deletado, verifique o ID.")
        logger.error(f"Tentativa de deletar produto falhou ID={produto_id}")

def mostrar_menu():
    """Exibe o menu principal"""
    print("\n=== Sistema de Produtos ===")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Atualizar produto")
    print("4 - Deletar produto")
    print("0 - Sair")

def main():
    create_table()
    print('=' * 5, "SISTEMA DE PRODUTOS", '=' * 5)

    acoes = {
        "1": cadastrar_produto,
        "2": mostrar_produtos,
        "3": atualizar_produto,
        "4": deletar_produtos_flow,
        "0": None
    }


        #algo simples para começar pegando os inputs
    while True:
        mostrar_menu()
        opcao_user = input("Digite uma opção -> ")
        acao = acoes.get(opcao_user)

        if acao is None and opcao_user == "0":
            print("Saindo do sistema...")
            break

        elif acao is None:
            print("Opção inválida.")
        
        else:
            acao()

if __name__ == "__main__":
    main()
    