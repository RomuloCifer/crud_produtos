from database import create_table
from repository import inserir_produto

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



if __name__ == "__main__":
    main()