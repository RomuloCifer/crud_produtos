from database import create_table
from repository import inserir_produto, listar_produtos, atualizar_produto


def cadastrar_produto():
    nome = input("Digite o nome do produto: ")
    preco = input("Digite o preço do produto: ")
    qtd = input("Digite a quantidade do produto: ")
    preco = float(preco)
    qtd = int(qtd)
    inserir_produto(nome, preco, qtd)
    print("\n",nome, "cadastrado com sucesso")

def mostrar_produtos():
    produtos = listar_produtos()
    if not produtos:
        print("Lista de produtos vazia.")
    else:
        for prod in produtos:
            prod_id, prod_nome, prod_preco, prod_qtd = prod
            print(f"ID:{prod_id} -> nome : {prod_nome} | preço : {prod_preco:.2f} | Quantidade : {prod_qtd}")

def atualizar_produtos():
    listar_produtos()
    id_str = input("Qual ID do produto que deseja alterar?")
    produto_id = int(id_str)

    print("Digite os novos dados. \n")
    novo_nome = input("Nome: ")
    preco = input("Preço: ")
    preco_float = float(preco)
    quantidade = input("Quantidade")
    qtd_int = int(quantidade)

    sucesso = atualizar_produto(produto_id, novo_nome, preco_float, qtd_int)
    if sucesso:
        print("Item atualizado com sucesso!")
    else:
        print("Nenhum produto atualizado, cheque o ID")

def mostrar_menu():
    """Exibe o menu principal"""
    print("\n=== Sistema de Produtos ===")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Atualizar produto")
    print("0 - Sair")

def main():
    create_table()
    print('=' * 5, "SISTEMA DE PRODUTOS", '=' * 5)

    #algo simples para começar pegando os inputs
    while True:
        mostrar_menu()
        opcao = input("Digite uma operação -> ")
        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            mostrar_produtos()
        elif opcao == "3":
            atualizar_produtos()
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    print(main())
    