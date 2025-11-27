
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

    @classmethod
    def find_active_by_user(cls, user_id: int):
        """
        Busca todos os empréstimos ativos de um usuário específico.
        Um empréstimo é considerado ativo se a data de devolução efetiva for NULA.
        """
        try:
            # Busca empréstimos onde a data de devolução efetiva é nula para o usuário
            emprestimos = cls.find_by({'usuario_id': user_id, 'data_devolucao_efetiva': None})

            # Para cada empréstimo, busca o exemplar e o livro correspondente
            from models.exemplar import Exemplar
            from models.livro import Livro

            for emprestimo in emprestimos:
                exemplar = Exemplar.find_by_id(emprestimo.exemplar_id)
                if exemplar:
                    livro = Livro.find_by_id(exemplar.livro_id)
                    exemplar.livro = livro  # Aninha o livro no exemplar
                emprestimo.exemplar = exemplar  # Aninha o exemplar no empréstimo

            return emprestimos
        except Exception as e:
            print(f"Erro ao buscar empréstimos ativos: {e}")
            return []

    @classmethod
    def find_history_by_user(cls, user_id: int):
        """
        Busca o histórico completo de empréstimos de um usuário.
        """
        try:
            emprestimos = cls.find_by({'usuario_id': user_id})

            from models.exemplar import Exemplar
            from models.livro import Livro

            for emprestimo in emprestimos:
                exemplar = Exemplar.find_by_id(emprestimo.exemplar_id)
                if exemplar:
                    livro = Livro.find_by_id(exemplar.livro_id)
                    exemplar.livro = livro
                emprestimo.exemplar = exemplar
                
                # Convert date strings to objects
                if emprestimo.data_emprestimo and isinstance(emprestimo.data_emprestimo, str):
                    try:
                        # Handle timezone 'Z' by replacing it with '+00:00'
                        if emprestimo.data_emprestimo.endswith('Z'):
                            emprestimo.data_emprestimo = emprestimo.data_emprestimo[:-1] + '+00:00'
                        emprestimo.data_emprestimo = datetime.fromisoformat(emprestimo.data_emprestimo)
                    except ValueError:
                        try:
                            # Fallback for formats without timezone
                            emprestimo.data_emprestimo = datetime.strptime(emprestimo.data_emprestimo, '%Y-%m-%d %H:%M:%S.%f')
                        except ValueError:
                             emprestimo.data_emprestimo = datetime.strptime(emprestimo.data_emprestimo, '%Y-%m-%d %H:%M:%S')

                if emprestimo.data_devolucao_prevista and isinstance(emprestimo.data_devolucao_prevista, str):
                    emprestimo.data_devolucao_prevista = date.fromisoformat(emprestimo.data_devolucao_prevista)
                
                if emprestimo.data_devolucao_efetiva and isinstance(emprestimo.data_devolucao_efetiva, str):
                    emprestimo.data_devolucao_efetiva = date.fromisoformat(emprestimo.data_devolucao_efetiva)

            return emprestimos
        except Exception as e:
            print(f"Erro ao buscar histórico de empréstimos: {e}")
            return []

    @classmethod
    def find_all_active_loans(cls):
        """
        Busca todos os empréstimos ativos.
        Um empréstimo é considerado ativo se a data de devolução efetiva for NULA.
        """
        try:
            # Busca empréstimos onde a data de devolução efetiva é nula
            emprestimos = cls.find_by({'data_devolucao_efetiva': None})

            # Para cada empréstimo, busca o exemplar e o livro correspondente
            from models.exemplar import Exemplar
            from models.livro import Livro
            from models.usuario import Usuario # Import for user details

            for emprestimo in emprestimos:
                exemplar = Exemplar.find_by_id(emprestimo.exemplar_id)
                if exemplar:
                    livro = Livro.find_by_id(exemplar.livro_id)
                    exemplar.livro = livro  # Aninha o livro no exemplar
                emprestimo.exemplar = exemplar  # Aninha o exemplar no empréstimo

                # Convert date strings to objects
                if emprestimo.data_emprestimo and isinstance(emprestimo.data_emprestimo, str):
                    try:
                        # Handle timezone 'Z' by replacing it with '+00:00'
                        if emprestimo.data_emprestimo.endswith('Z'):
                            emprestimo.data_emprestimo = emprestimo.data_emprestimo[:-1] + '+00:00'
                        emprestimo.data_emprestimo = datetime.fromisoformat(emprestimo.data_emprestimo)
                    except ValueError:
                        try:
                            # Fallback for formats without timezone
                            emprestimo.data_emprestimo = datetime.strptime(emprestimo.data_emprestimo, '%Y-%m-%d %H:%M:%S.%f')
                        except ValueError:
                             emprestimo.data_emprestimo = datetime.strptime(emprestimo.data_emprestimo, '%Y-%m-%d %H:%M:%S')

                if emprestimo.data_devolucao_prevista and isinstance(emprestimo.data_devolucao_prevista, str):
                    emprestimo.data_devolucao_prevista = date.fromisoformat(emprestimo.data_devolucao_prevista)


                # Get user details for the loan
                usuario = Usuario.find_by_id(emprestimo.usuario_id)
                emprestimo.usuario = usuario # Aninha o usuario no empréstimo

            return emprestimos
        except Exception as e:
            print(f"Erro ao buscar todos os empréstimos ativos: {e}")
            return []

    @classmethod
    def has_overdue_books(cls, user_id: int) -> bool:
        """
        Verifica se um usuário possui livros com devolução em atraso.
        """
        active_loans = cls.find_active_by_user(user_id)
        today = date.today()
        for loan in active_loans:
            if loan.data_devolucao_prevista < today:
                return True
        return False
