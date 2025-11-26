
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
        super().__init__(
            livro_id=livro_id,
            titulo=titulo,
            autor=autor,
            editora=editora,
            ano_publicacao=ano_publicacao
        )

    @property
    def livro_id(self) -> int:
        return self._livro_id

    @livro_id.setter
    def livro_id(self, value: int):
        self._livro_id = value

    @property
    def titulo(self) -> str:
        return self._titulo

    @titulo.setter
    def titulo(self, value: str):
        self._titulo = value

    @property
    def autor(self) -> str:
        return self._autor

    @autor.setter
    def autor(self, value: str):
        self._autor = value

    @property
    def editora(self) -> str:
        return self._editora

    @editora.setter
    def editora(self, value: str):
        self._editora = value

    @property
    def ano_publicacao(self) -> int:
        return self._ano_publicacao

    @ano_publicacao.setter
    def ano_publicacao(self, value: int):
        self._ano_publicacao = value

    @classmethod
    def search(cls, search_terms: dict):
        """
        Busca livros no banco de dados com base em termos de pesquisa parciais e insensíveis a maiúsculas/minúsculas.
        """
        try:
            query = cls.get_query()
            for column, value in search_terms.items():
                query = query.ilike(column, f"%{value}%")
            
            result = query.execute()
            
            if result.data:
                return [cls(**item) for item in result.data]
            return []
        except Exception as e:
            print(f"Erro ao buscar livros: {e}")
            return []
