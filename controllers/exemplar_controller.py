from models.exemplar import Exemplar
from models.livro import Livro
from controllers.livro_controller import LivroController
from views import exemplar_view


class ExemplarController:
    def __init__(self):
        self.__livros = LivroController()

    """
    Controlador para a gestão de exemplares.
    """

    def adicionar_exemplar(self):
        """
        Orquestra o processo de adicionar um novo exemplar.
        """
        self.__livros.listar_livros()
        dados_exemplar = exemplar_view.get_exemplar_info()

        # Validação: Verifica se o livro associado ao exemplar realmente existe
        livro_id = dados_exemplar.get("livro_id")
        livro_existente = Livro.find_by_id(livro_id)

        if not livro_existente:
            print(
                f"\nErro: Nenhum livro encontrado com o ID {livro_id}. O exemplar não pode ser cadastrado."
            )
            return

        exemplar = Exemplar(exemplar_nome=livro_existente.titulo, **dados_exemplar)
        exemplar.save()
        exemplar_view.show_exemplar_criado(exemplar)

    def listar_exemplares(self):
        """
        Orquestra a listagem de todos os exemplares.
        1. Busca todos os livros usando o modelo Exemplar.
        2. Envia a lista de exemplares para a View exibi-los.
        """
        exemplares = Exemplar.find_all()
        exemplar_view.display_exemplares(exemplares)

    def listar_exemplares_disponiveis(self):
        """
        Orquestra a listagem de todos os exemplares disponíveis.
        """
        exemplares = Exemplar.find_all()
        exemplares_disponiveis = [e for e in exemplares if e.disponivel]
        exemplar_view.display_exemplares(exemplares_disponiveis)

    def atualizar_exemplar(self):
        """
        Orquestra a atualização de um exemplar cadastrado.
        """
        # Primeiro, lista os exemplares para o usuário saber qual ID usar
        self.listar_exemplares()
        exemplares = Exemplar.find_all()
        if not exemplares:
            return

        exemplar_id = exemplar_view.get_exemplar_id_para_operacao("atualizar")
        exemplar = Exemplar.find_by_id(exemplar_id)

        if not exemplar:
            print("\nExemplar não encontrado!")
            return

        novos_dados = exemplar_view.get_dados_atualizacao_exemplar(exemplar)

        # Atualiza os atributos do objeto exemplar
        exemplar.livro_id = novos_dados["livro_id"]
        exemplar.localizacao = novos_dados["localizacao"]
        exemplar.disponivel = novos_dados["disponivel"]

        exemplar.save()  # O save() fará o update
        exemplar_view.show_exemplar_atualizado(exemplar)

    def deletar_exemplar(self):
        """
        Orquesta a exclusão de um exemplar cadastrado.
        """
        # Lista os exemplares para o usuário saber qual ID deletar
        self.listar_exemplares()
        exemplar = Exemplar.find_all()
        if not exemplar:
            return

        exemplar_id = exemplar_view.get_exemplar_id_para_operacao("deletar")
        exemplar = Exemplar.find_by_id(exemplar_id)

        if not exemplar:
            print("\nExemplar não encontrado!")
            return

        exemplar.delete()
        exemplar_view.show_exemplar_deletado(exemplar_id)
