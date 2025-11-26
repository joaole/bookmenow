from models.emprestimo import Emprestimo
from views.emprestimo_view import display_emprestimos

class EmprestimoController:
    def listar_emprestimos_ativos(self, usuario):
        """
        Lista os empréstimos ativos para o usuário logado.
        """
        emprestimos = Emprestimo.find_active_by_user(usuario.id)
        display_emprestimos(emprestimos)

    def listar_historico_emprestimos(self, usuario):
        """
        Lista o histórico de empréstimos para o usuário logado.
        """
        emprestimos = Emprestimo.find_history_by_user(usuario.id)
        display_emprestimos(emprestimos, historico=True)
