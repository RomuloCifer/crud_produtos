from database import create_table
from repository import inserir_produto, listar_produtos

def main():
    create_table()
    print('=' * 5, "SISTEMA DE PRODUTOS", '=' * 5)

    #algo simples para começar pegando os inputs
    nome = input("Digite o nome do produto: ")
    preco = input("Digite o preço do produto: ")
    qtd = input("Digite a quantidade do produto: ")
    preco = float(preco)
    qtd = int(qtd)
    inserir_produto(nome, preco, qtd)
    print("\n",nome, "cadastrado com sucesso")

    produtos = listar_produtos()
    if not produtos:
        print("Lista de produtos vazia.")
    else:
        for prod in produtos:
            prod_id, prod_nome, prod_preco, prod_qtd = prod

            print(f"ID:{prod_id} -> nome : {prod_nome} | preço : {prod_preco:.2f} | Quantidade : {prod_qtd}")

if __name__ == "__main__":
    print(main())
    