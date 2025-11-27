import json
from typing import List, Dict, Any
from models.exemplar import Exemplar


def display_exemplares(exemplares: List[Exemplar]) -> None:
    """
    Exibe uma lista de exemplares no terminal de forma formatada.

    Args:
        exemplares: Uma lista de objetos Exemplar.
    """
    if not exemplares:
        print("\nNenhum exemplar cadastrado")
        return

    print("\n--- Lista de Exemplares ---")
    for exemplar in exemplares:
        print(f"ID: {exemplar.id}")
        print(f"Nome do livro: {exemplar.exemplar_nome}")
        print(f"ID do livro: {exemplar.livro_id}")
        print(f"Localização: {exemplar.localizacao}")
        print(f"Disponibilidade: {exemplar.disponivel}")
        print("-" * 20)


def get_exemplar_info() -> Dict[str, Any]:
    """
    Solicita ao usuário as informações para cadastrar um novo exemplar.

    Returns:
        Um dicionário com os dados do exemplar.
    """
    print("\n--- Cadastro de Novo Exemplar ---")

    while True:
        try:
            livro_id_str = input(
                "Digite o ID do livro ao qual este exemplar pertence: "
            )
            livro_id = int(livro_id_str)

            break
        except ValueError:
            print("ID do livro inválido. Por favor, digite um número.")

    print("\nInsira a localização do exemplar")
    while True:
        try:
            corredor = int(input("Digite o corredor onde exemplar se encontra: "))
            prateleira = int(input("Digite sua prateleira: "))
            localizacao_str = f'{{"corredor": {corredor}, "prateleira": {prateleira}}}'
            localizacao = json.loads(localizacao_str)
            # if not isinstance(corredor, int) or not isinstance(prateleira, int):
            #     raise ValueError("Valor inserido inválido")
            break
        except ValueError:
            print("Entrada inválida, somente números \n")

    return {"livro_id": livro_id, "localizacao": localizacao}


def get_exemplar_id_para_operacao(operacao: str) -> int:
    """
    Solicita ao usuário o ID de um livro para uma operação específica (ex: deletar).
    Args:
        operacao: Ação que será realizada (ex: "deletar", "atualizar").
    Returns:
        O ID do livro informado pelo usuário.
    """
    while True:
        try:
            id_str = input(f"\nID do exemplar que deseja {operacao}: ")
            return int(id_str)
        except ValueError:
            print("ID inválido. Por favor, digite um número")


def get_dados_atualizacao_exemplar(exemplar: Exemplar) -> Dict[str, Any]:
    """
    Solicita ao usuário os novos dados para atualizar um exemplar, mostrando os valores atuais.
    Args:
        exemplar: O objeto Livro a ser atualizado.
    Returns:
        Um dicionário com os novos dados.
    """
    print("\n--- Atualização do Exemplar ---")
    print("Deixe o campo em branco manter o valor atual.")

    livro_id = input(f"ID livro [{exemplar.livro_id}]: ") or exemplar.livro_id
    localizacao = (
        input(f"localização [{exemplar.localizacao}]: ") or exemplar.localizacao
    )
    disponivel = (
        input(f"disponibilidade [{exemplar.disponivel}]: ") or exemplar.disponivel
    )

    return {"livro_id": livro_id, "localizacao": localizacao, "disponivel": disponivel}


def show_exemplar_criado(exemplar):
    print(
        f"\nExemplar (ID: {exemplar.id}) para o livro ID {exemplar.livro_id} cadastrado com sucesso!"
    )


def show_exemplar_atualizado(exemplar):
    print(f"\nExemplar '{exemplar.id}' atualizado com sucesso!")


def show_exemplar_deletado(exemplar_id: int):
    print(f"\nExemplar '{exemplar_id}' deletado com sucesso!")
