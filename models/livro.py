
from models.base_model import BaseModel

class Livro(BaseModel):
    """
    Representa a tabela 'livros' no banco de dados.
    Herda de BaseModel para obter a funcionalidade ORM.
    """
    # Nome da tabela no Supabase
    table_name = "livros"
    # Nome da chave primária da tabela
    primary_key = "livro_id"

    def __init__(self, titulo: str, autor: str = None, editora: str = None, ano_publicacao: int = None, livro_id: int = None):
        """
        Inicializa uma instância de Livro.

        Args:
            titulo (str): O título do livro.
            autor (str, optional): O autor do livro. Defaults to None.
            editora (str, optional): A editora do livro. Defaults to None.
            ano_publicacao (int, optional): O ano de publicação. Defaults to None.
            livro_id (int, optional): O ID do livro (usado ao carregar do banco). Defaults to None.
        """
        super().__init__()
        self.livro_id = livro_id
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.ano_publicacao = ano_publicacao
