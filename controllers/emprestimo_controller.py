from datetime import date, timedelta
from models.emprestimo import Emprestimo
from models.usuario import Usuario
from models.exemplar import Exemplar
from views.emprestimo_view import display_emprestimos, get_emprestimo_info, get_devolucao_info

class EmprestimoController:
    def registrar_emprestimo(self):
        """
        Orquestra o processo de registrar um novo empréstimo.
        """
        dados = get_emprestimo_info()
        usuario_id = dados['usuario_id']
        exemplar_id = dados['exemplar_id']

        usuario = Usuario.find_by_id(usuario_id)
        if not usuario:
            print("Usuário não encontrado.")
            return

        if Emprestimo.has_overdue_books(usuario_id):
            print("Este usuário possui livros com devolução em atraso e não pode realizar novos empréstimos.")
            return

        exemplar = Exemplar.find_by_id(exemplar_id)
        if not exemplar:
            print("Exemplar não encontrado.")
            return

        if not exemplar.disponivel:
            print("Este exemplar não está disponível para empréstimo.")
            return
        
        data_emprestimo = date.today()
        data_devolucao_prevista = data_emprestimo + timedelta(days=14)

        novo_emprestimo = Emprestimo(
            usuario_id=usuario_id,
            exemplar_id=exemplar.id,
            data_devolucao_prevista=data_devolucao_prevista
        )
        novo_emprestimo.save()

        exemplar.disponivel = False
        exemplar.save()

        print("Empréstimo registrado com sucesso!")

    def registrar_devolucao(self):
        """
        Orquestra o processo de registrar a devolução de um livro.
        """
        emprestimo_id = get_devolucao_info()
        emprestimo = Emprestimo.find_by_id(emprestimo_id)

        if not emprestimo:
            print("Empréstimo não encontrado.")
            return

        emprestimo.data_devolucao_efetiva = date.today()
        emprestimo.save()

        exemplar = Exemplar.find_by_id(emprestimo.exemplar_id)
        if exemplar:
            exemplar.disponivel = True
            exemplar.save()

        print("Devolução registrada com sucesso!")

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
