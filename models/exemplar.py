
from typing import Dict
from models.base_model import BaseModel

class Exemplar(BaseModel):
    """
    Representa a tabela 'exemplares' no banco de dados.
    """
    table_name = "exemplares"
    primary_key = "id"

    def __init__(self, livro_id: int, localizacao: Dict, disponivel: bool = True, id: int = None):
        super().__init__(
            id=id,
            livro_id=livro_id,
            localizacao=localizacao,
            disponivel=disponivel
        )

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value

    @property
    def livro_id(self) -> int:
        return self._livro_id

    @livro_id.setter
    def livro_id(self, value: int):
        self._livro_id = value

    @property
    def localizacao(self) -> Dict:
        return self._localizacao

    @localizacao.setter
    def localizacao(self, value: Dict):
        self._localizacao = value

    @property
    def disponivel(self) -> bool:
        return self._disponivel

    @disponivel.setter
    def disponivel(self, value: bool):
        self._disponivel = value

    @classmethod
    def find_available_by_book(cls, livro_id: int):
        """
        Busca todos os exemplares disponíveis de um livro específico.
        """
        return cls.find_by({'livro_id': livro_id, 'disponivel': True})
