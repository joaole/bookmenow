from models.exemplar import Exemplar
from models.livro import Livro
from views import exemplar_view

class ExemplarController:
    """
    Controlador para a gestão de exemplares.
    """

    def adicionar_exemplar(self):
        """
        Orquestra o processo de adicionar um novo exemplar.
        """
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
