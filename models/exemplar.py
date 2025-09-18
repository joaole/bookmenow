
from typing import Dict
from models.base_model import BaseModel

class Exemplar(BaseModel):
    """
    Representa a tabela 'exemplares' no banco de dados.
    """
    table_name = "exemplares"
    primary_key = "id"

    def __init__(self, livro_id: int, localizacao: Dict, disponivel: bool = True, id: int = None):
        """
        Inicializa uma instância de Exemplar.

        Args:
            livro_id (int): ID do livro ao qual este exemplar pertence.
            localizacao (Dict): Objeto JSON com a localização (ex: {"corredor": 5, "prateleira": "B"}).
            disponivel (bool, optional): Status de disponibilidade. Defaults to True.
            id (int, optional): O ID do exemplar. Defaults to None.
        """
        super().__init__()
        self.id = id
        self.livro_id = livro_id
        self.localizacao = localizacao
        self.disponivel = disponivel
