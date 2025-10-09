
from datetime import date, datetime
from models.base_model import BaseModel

class Emprestimo(BaseModel):
    """
    Representa a tabela 'emprestimos' no banco de dados.
    """
    table_name = "emprestimos"
    primary_key = "id"

    def __init__(self, usuario_id: int, exemplar_id: int, data_devolucao_prevista: date, id: int = None, data_emprestimo: datetime = None, data_devolucao_efetiva: date = None):
        super().__init__(
            id=id,
            usuario_id=usuario_id,
            exemplar_id=exemplar_id,
            data_emprestimo=data_emprestimo,
            data_devolucao_prevista=data_devolucao_prevista,
            data_devolucao_efetiva=data_devolucao_efetiva
        )

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value

    @property
    def usuario_id(self) -> int:
        return self._usuario_id

    @usuario_id.setter
    def usuario_id(self, value: int):
        self._usuario_id = value

    @property
    def exemplar_id(self) -> int:
        return self._exemplar_id

    @exemplar_id.setter
    def exemplar_id(self, value: int):
        self._exemplar_id = value

    @property
    def data_emprestimo(self) -> datetime:
        return self._data_emprestimo

    @data_emprestimo.setter
    def data_emprestimo(self, value: datetime):
        self._data_emprestimo = value

    @property
    def data_devolucao_prevista(self) -> date:
        return self._data_devolucao_prevista

    @data_devolucao_prevista.setter
    def data_devolucao_prevista(self, value: date):
        self._data_devolucao_prevista = value

    @property
    def data_devolucao_efetiva(self) -> date:
        return self._data_devolucao_efetiva

    @data_devolucao_efetiva.setter
    def data_devolucao_efetiva(self, value: date):
        self._data_devolucao_efetiva = value

