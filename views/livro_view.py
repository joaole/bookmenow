from typing import List, Dict, Any
from models.livro import Livro

def display_livros(livros: List[Livro]) -> None:
    """
    Exibe uma lista de livros no terminal de forma formatada.

    Args:
        livros: Uma lista de objetos Livro.
    """
    if not livros:
        print("\nNenhum livro encontrado.")
        return

    print("\n--- Lista de Livros ---")
    for livro in livros:
        print(f"ID: {livro.livro_id}")
        print(f"  Título: {livro.titulo}")
        print(f"  Autor: {livro.autor or 'Não informado'}")
        print(f"  Editora: {livro.editora or 'Não informada'}")
        print(f"  Ano: {livro.ano_publicacao or 'Não informado'}")
        print("-" * 20)

def get_livro_info() -> Dict[str, Any]:
    """
    Solicita ao usuário as informações para cadastrar um novo livro.

    Returns:
        Um dicionário com os dados do livro.
    """
    print("\n--- Cadastro de Novo Livro ---")
    titulo = input("Título: ")
    autor = input("Autor: ")
    editora = input("Editora: ")
    ano_publicacao_str = input("Ano de Publicação: ")

    # Validação simples
    ano_publicacao = int(ano_publicacao_str) if ano_publicacao_str.isdigit() else None

    return {
        "titulo": titulo,
        "autor": autor,
        "editora": editora,
        "ano_publicacao": ano_publicacao
    }

def get_livro_id_para_operacao(operacao: str) -> int:
    """
    Solicita ao usuário o ID de um livro para uma operação específica (ex: deletar).

    Args:
        operacao: Ação que será realizada (ex: "deletar", "atualizar").

    Returns:
        O ID do livro informado pelo usuário.
    """
    while True:
        try:
            id_str = input(f"\nDigite o ID do livro que deseja {operacao}: ")
            return int(id_str)
        except ValueError:
            print("ID inválido. Por favor, digite um número.")

def get_dados_atualizacao_livro(livro: Livro) -> Dict[str, Any]:
    """
    Solicita ao usuário os novos dados para atualizar um livro, mostrando os valores atuais.

    Args:
        livro: O objeto Livro a ser atualizado.

    Returns:
        Um dicionário com os novos dados.
    """
    print("\n--- Atualização de Livro ---")
    print("Deixe o campo em branco para manter o valor atual.")

    titulo = input(f"Título [{livro.titulo}]: ") or livro.titulo
    autor = input(f"Autor [{livro.autor or 'N/A'}]: ") or livro.autor
    editora = input(f"Editora [{livro.editora or 'N/A'}]: ") or livro.editora
    ano_str = input(f"Ano [{livro.ano_publicacao or 'N/A'}]: ")

    ano_publicacao = int(ano_str) if ano_str.isdigit() else livro.ano_publicacao

    return {
        "titulo": titulo,
        "autor": autor,
        "editora": editora,
        "ano_publicacao": ano_publicacao
    }

def show_livro_criado(livro: Livro):
    print(f"\nLivro '{livro.titulo}' (ID: {livro.livro_id}) cadastrado com sucesso!")

def show_livro_atualizado(livro: Livro):
    print(f"\nLivro '{livro.titulo}' (ID: {livro.livro_id}) atualizado com sucesso!")

def show_livro_deletado(livro_id: int):
    print(f"\nLivro com ID {livro_id} deletado com sucesso!")


def get_titulo_busca() -> str:
    """Solicita ao usuário o título para busca."""
    return input("Digite o título do livro que você está buscando: ")


def get_autor_busca() -> str:
    """Solicita ao usuário o autor para busca."""
    return input("Digite o nome do autor que você está buscando: ")


