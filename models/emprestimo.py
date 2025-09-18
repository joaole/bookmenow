
from datetime import date, datetime
from models.base_model import BaseModel

class Emprestimo(BaseModel):
    """
    Representa a tabela 'emprestimos' no banco de dados.
    """
    table_name = "emprestimos"
    primary_key = "id"

    def __init__(self, usuario_id: int, exemplar_id: int, data_devolucao_prevista: date, id: int = None, data_emprestimo: datetime = None, data_devolucao_efetiva: date = None):
        """
        Inicializa uma instância de Emprestimo.

        Args:
            usuario_id (int): ID do usuário que fez o empréstimo.
            exemplar_id (int): ID do exemplar emprestado.
            data_devolucao_prevista (date): Data prevista para a devolução.
            id (int, optional): O ID do empréstimo. Defaults to None.
            data_emprestimo (datetime, optional): Data em que o empréstimo foi feito. Defaults to None.
            data_devolucao_efetiva (date, optional): Data em que o livro foi devolvido. Defaults to None.
        """
        super().__init__()
        self.id = id
        self.usuario_id = usuario_id
        self.exemplar_id = exemplar_id
        self.data_emprestimo = data_emprestimo
        self.data_devolucao_prevista = data_devolucao_prevista
        self.data_devolucao_efetiva = data_devolucao_efetiva
