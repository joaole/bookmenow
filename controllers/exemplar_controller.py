from models.exemplar import Exemplar
from models.livro import Livro
from controllers.livro_controller import LivroController
from views import exemplar_view

class ExemplarController:
    def __init__(self):
        self.livro_controller = LivroController
    """
    Controlador para a gestão de exemplares.
    """

    def adicionar_exemplar(self):
        """
        Orquestra o processo de adicionar um novo exemplar.
        """
        self.livro_controller.listar_livros
        dados_exemplar = exemplar_view.get_exemplar_info()

        # Validação: Verifica se o livro associado ao exemplar realmente existe
        livro_id = dados_exemplar.get("livro_id")
        livro_existente = Livro.find_by_id(livro_id)

        if not livro_existente:
            print(f"\nErro: Nenhum livro encontrado com o ID {livro_id}. O exemplar não pode ser cadastrado.")
            return

        exemplar = Exemplar(**dados_exemplar)
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

    def atualizar_exemplar(self):
        """
        Orquestra a atualização de um exemplar cadastrado.
        """
        # Primeiro, lista os exemplares para o usuário saber qual ID usar