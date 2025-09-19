import json
from typing import List, Dict, Any
from models.exemplar import Exemplar
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
            livro_id_str = input("Digite o ID do livro ao qual este exemplar pertence: ")
            livro_id = int(livro_id_str)

            break
        except ValueError:
            print("ID do livro inválido. Por favor, digite um número.")

    print("\nDigite a localização do exemplar (formato JSON).")
    print('Exemplo: {"corredor": 5, "prateleira": "3"}')
    while True:
        try:
            localizacao_str = input("Localização (JSON): ")
            localizacao = json.loads(localizacao_str)
            if not isinstance(localizacao, dict):
                raise ValueError("O JSON deve ser um objeto (dicionário).")
            break
        except json.JSONDecodeError:
            print("Formato JSON inválido. Tente novamente.")
        except ValueError as e:
            print(e)

    return {
        "livro_id": livro_id,
        "localizacao": localizacao
    }

def show_exemplar_criado(exemplar):
    print(f"\nExemplar (ID: {exemplar.id}) para o livro ID {exemplar.livro_id} cadastrado com sucesso!")
