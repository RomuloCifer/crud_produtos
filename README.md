# Sistema de Gerenciamento de Produtos

Sistema CRUD (Create, Read, Update, Delete) para gerenciamento de produtos desenvolvido em Python com SQLite.

## 📋 Funcionalidades

- ✅ Cadastrar novos produtos (nome, preço, quantidade)
- 📋 Listar todos os produtos cadastrados
- ✏️ Atualizar informações de produtos existentes
- 🗑️ Deletar produtos do sistema
- 📝 Sistema de logging para rastreamento de operações

## 🛠️ Tecnologias

- **Python 3.x**
- **SQLite** - Banco de dados embutido
- **unittest** - Testes unitários
- **dataclasses** - Estruturação de dados

## 📁 Estrutura do Projeto

```
crud_produtos/
├── main.py              # Interface principal e menu do sistema
├── produto.py           # Classe Produto (modelo de dados)
├── repository.py        # Operações CRUD no banco de dados
├── database.py          # Configuração e conexão com SQLite
├── logger.py            # Sistema de logging de operações
├── test_produtos.py     # Testes unitários
└── README.md           # Documentação do projeto
```

## 🚀 Como Executar

### Pré-requisitos
- Python 3.7 ou superior instalado

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/RomuloCifer/crud_produtos.git
cd crud_produtos
```

2. Execute o programa:
```bash
python main.py
```

## 💻 Uso do Sistema

Ao executar o programa, você verá o menu interativo:

```
=== Sistema de Produtos ===
1 - Cadastrar produto
2 - Listar produtos
3 - Atualizar produto
4 - Deletar produto
0 - Sair
```

### Exemplos de Uso

**Cadastrar produto:**
- Selecione opção 1
- Digite o nome do produto
- Digite o preço (aceita vírgula ou ponto)
- Digite a quantidade em estoque

**Listar produtos:**
- Selecione opção 2
- Visualize todos os produtos com ID, nome, preço e quantidade

**Atualizar produto:**
- Selecione opção 3
- Escolha o ID do produto a atualizar
- Digite os novos dados

**Deletar produto:**
- Selecione opção 4
- Digite o ID do produto
- Confirme a exclusão

## 🧪 Testes

Execute os testes unitários:

```bash
python -m unittest test_produtos.py
```

Ou execute diretamente:

```bash
python test_produtos.py
```

## 📝 Sistema de Logs

Todas as operações são registradas no arquivo `produtos.log` com timestamp:
- `[CREATE]` - Produtos cadastrados
- `[UPDATE]` - Produtos atualizados
- `[DELETE]` - Produtos deletados
- `[ERRO]` - Operações com falha

## 🗄️ Banco de Dados

O sistema utiliza SQLite com a seguinte estrutura:

**Tabela: produtos**
| Campo      | Tipo    | Descrição                     |
|------------|---------|-------------------------------|
| id         | INTEGER | Chave primária (auto-increment) |
| nome       | TEXT    | Nome do produto               |
| preco      | REAL    | Preço do produto              |
| quantidade | INTEGER | Quantidade em estoque         |

O banco de dados é criado automaticamente no arquivo `produtos.db` na primeira execução.

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:
1. Fazer um fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abrir um Pull Request

## 👤 Autor

**Romulo Cifer**
- GitHub: [@RomuloCifer](https://github.com/RomuloCifer)

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

---

⭐ Desenvolvido com Python
