from models.livro import Livro
from views import livro_view


class LivroController:
    """
    Controlador para a gestão de livros.
    Orquestra a interação entre a View (terminal) e o Model (Livro).
    """

    def adicionar_livro(self):
        """
        Orquestra o processo de adicionar um novo livro.
        1. Pede os dados do livro à View.
        2. Cria uma instância do modelo Livro.
        3. Salva o livro no banco de dados.
        4. Informa o resultado na View.
        """
        dados_livro = livro_view.get_livro_info()

        # Garante que o título não seja vazio
        if not dados_livro.get("titulo"):
            print("\nO título é obrigatório!")
            return

        livro = Livro(**dados_livro)
        livro.save()
        livro_view.show_livro_criado(livro)

    def listar_livros(self):
        """
        Orquestra a listagem de todos os livros.
        1. Busca todos os livros usando o modelo Livro.
        2. Envia a lista de livros para a View exibi-los.
        """
        livros = Livro.find_all()
        livro_view.display_livros(livros)

    def atualizar_livro(self):
        """
        Orquestra a atualização de um livro existente.
        """
        # Primeiro, lista os livros para o usuário saber qual ID usar
        self.listar_livros()
        livros = Livro.find_all()
        if not livros:
            return

        livro_id = livro_view.get_livro_id_para_operacao("atualizar")
        livro = Livro.find_by_id(livro_id)

        if not livro:
            print("\nLivro não encontrado!")
            return

        novos_dados = livro_view.get_dados_atualizacao_livro(livro)

        # Atualiza os atributos do objeto livro
        livro.titulo = novos_dados["titulo"]
        livro.autor = novos_dados["autor"]
        livro.editora = novos_dados["editora"]
        livro.ano_publicacao = novos_dados["ano_publicacao"]

        livro.save()  # O método save() fará o UPDATE
        livro_view.show_livro_atualizado(livro)

    def deletar_livro(self):
        """
        Orquestra a exclusão de um livro.
        """
        # Lista os livros para o usuário saber qual ID deletar
        self.listar_livros()
        livros = Livro.find_all()
        if not livros:
            return

        livro_id = livro_view.get_livro_id_para_operacao("deletar")
        livro = Livro.find_by_id(livro_id)

        if not livro:
            print("\nLivro não encontrado!")
            return

        livro.delete()
        livro_view.show_livro_deletado(livro_id)

    def buscar_livro_por_titulo(self):
        """
        Busca um livro pelo título.
        """
        titulo = livro_view.get_titulo_busca()
        livros = Livro.search({"titulo": titulo})
        livro_view.display_livros(livros)

    def buscar_livro_por_autor(self):
        """
        Busca um livro pelo autor.
        """
        autor = livro_view.get_autor_busca()
        livros = Livro.search({"autor": autor})
        livro_view.display_livros(livros)
