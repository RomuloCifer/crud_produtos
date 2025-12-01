from dataclasses import dataclass
from typing import Optional # Para tipos opcionais  


@dataclass 
class Produto:
    """Classe que representa um produto com nome, preço e quantidade."""
    id: Optional[int]  # ID pode ser None quando o produto ainda não foi salvo no banco de dados
    nome: str
    preco: float
    quantidade: int