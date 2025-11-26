from typing import List
from models.emprestimo import Emprestimo

def display_emprestimos(emprestimos: List[Emprestimo], historico: bool = False):
    """
    Exibe uma lista de empréstimos (ativos ou histórico) no terminal.
    """
    if not emprestimos:
        if historico:
            print("\nVocê não possui histórico de empréstimos.")
        else:
            print("\nVocê não possui empréstimos ativos.")
        return

    titulo_menu = "Histórico de Empréstimos" if historico else "Meus Empréstimos Ativos"
    print(f"\n--- {titulo_menu} ---")

    for emprestimo in emprestimos:
        livro = emprestimo.exemplar.livro
        print(f"ID do Empréstimo: {emprestimo.id}")
        print(f"  Título: {livro.titulo}")
        print(f"  Autor: {livro.autor}")
        print(f"  Data do Empréstimo: {emprestimo.data_emprestimo}")
        print(f"  Data de Devolução Prevista: {emprestimo.data_devolucao_prevista}")
        if historico and emprestimo.data_devolucao_efetiva:
            print(f"  Data de Devolução Efetiva: {emprestimo.data_devolucao_efetiva}")
        print("-" * 20)

def get_emprestimo_info():
    """
    Solicita ao administrador o ID do usuário e do exemplar para um novo empréstimo.
    """
    print("\n--- Registrar Novo Empréstimo ---")
    while True:
        try:
            usuario_id = int(input("Digite o ID do usuário: "))
            exemplar_id = int(input("Digite o ID do exemplar: "))
            return {"usuario_id": usuario_id, "exemplar_id": exemplar_id}
        except ValueError:
            print("IDs inválidos. Por favor, digite números inteiros.")

def get_devolucao_info():
    """
    Solicita ao administrador o ID do empréstimo a ser devolvido.
    """
    print("\n--- Registrar Devolução ---")
    while True:
        try:
            emprestimo_id = int(input("Digite o ID do empréstimo a ser devolvido: "))
            return emprestimo_id
        except ValueError:
            print("ID inválido. Por favor, digite um número inteiro.")

