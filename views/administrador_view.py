from typing import List, Dict, Any
from models.usuario import Usuario
from datetime import datetime, date

def display_usuarios(usuarios: List[Usuario]) -> None:
    """
    Exibe uma lista de usuários no terminal de forma formatada.

    Args:
        usuarios: Uma lista de objetos Usuario.
    """
    if not usuarios:
        print("\nNenhum usuário encontrado.")
        return

    print("\n--- Lista de Usuários ---")
    for usuario in usuarios:
        print(f"ID: {usuario.id}")
        print(f"  Nome: {usuario.nome}")
        print(f"  Email: {usuario.email}")
        print(f"  Matrícula: {usuario.matricula}")
        if hasattr(usuario, 'cargo') and usuario.cargo:
            print(f"  Cargo: {usuario.cargo}")
        print(f"  Tipo: {usuario.tipo_usuario}")
        print(f"  Ativo: {'Sim' if usuario.ativo else 'Não'}")
        print("-" * 20)

def get_usuario_info() -> Dict[str, Any]:
    """
    Solicita ao usuário as informações para cadastrar um novo usuário.

    Returns:
        Um dicionário com os dados do usuário.
    """
    print("\n--- Cadastro de Novo Usuário ---")
    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")
    telefone = input("Telefone: ")
    endereco = input("Endereço: ")
    while True:
        tipo_usuario = input("Tipo de usuário (leitor/administrador): ").lower()
        if tipo_usuario in ["leitor", "administrador"]:
            break
        else:
            print("Tipo de usuário inválido. Tente novamente.")
    cargo = input("Cargo (opcional): ")

    return {
        "nome": nome,
        "email": email,
        "senha": senha,
        "telefone": telefone,
        "endereco": endereco,
        "tipo_usuario": tipo_usuario,
        "cargo": cargo
    }

def get_usuario_id_para_operacao(operacao: str) -> int:
    """
    Solicita ao usuário o ID de um usuário para uma operação específica.

    Args:
        operacao: Ação que será realizada (ex: "deletar", "atualizar").

    Returns:
        O ID do usuário informado pelo usuário.
    """
    while True:
        try:
            id_str = input(f"\nDigite o ID do usuário que deseja {operacao}: ")
            return int(id_str)
        except ValueError:
            print("ID inválido. Por favor, digite um número.")

def get_dados_atualizacao_usuario(usuario: Usuario) -> Dict[str, Any]:
    """
    Solicita ao usuário os novos dados para atualizar um usuário, mostrando os valores atuais.

    Args:
        usuario: O objeto Usuario a ser atualizado.

    Returns:
        Um dicionário com os novos dados.
    """
    print("\n--- Atualização de Usuário ---")
    print("Deixe o campo em branco para manter o valor atual.")

    nome = input(f"Nome [{usuario.nome}]: ") or usuario.nome
    email = input(f"Email [{usuario.email}]: ") or usuario.email
    telefone = input(f"Telefone [{usuario.telefone}]: ") or usuario.telefone
    endereco = input(f"Endereço [{usuario.endereco}]: ") or usuario.endereco
    cargo = input(f"Cargo [{usuario.cargo or 'N/A'}]: ") or usuario.cargo
    
    while True:
        ativo_str = input(f"Ativo (s/n) [{ 's' if usuario.ativo else 'n'}]: ").lower()
        if ativo_str in ['s', 'n', '']:
            break
        else:
            print("Opção inválida. Digite 's' ou 'n'.")

    ativo = usuario.ativo
    if ativo_str == 's':
        ativo = True
    elif ativo_str == 'n':
        ativo = False

    return {
        "nome": nome,
        "email": email,
        "telefone": telefone,
        "endereco": endereco,
        "cargo": cargo,
        "ativo": ativo
    }

def show_usuario_criado(usuario: Usuario):
    print(f"\nUsuário '{usuario.nome}' (ID: {usuario.id}) cadastrado com sucesso!")

def show_usuario_atualizado(usuario: Usuario):
    print(f"\nUsuário '{usuario.nome}' (ID: {usuario.id}) atualizado com sucesso!")

def show_usuario_desativado(usuario_id: int):
    print(f"\nUsuário com ID {usuario_id} desativado com sucesso!")

def menu_listar_usuarios() -> str:
    """
    Exibe um menu de opções de filtro para a listagem de usuários.

    Returns:
        A opção de filtro escolhida pelo usuário.
    """
    print("\n--- Opções de Listagem ---")
    print("1 - Listar todos")
    print("2 - Listar apenas administradores")
    print("3 - Listar apenas leitores")
    print("4 - Listar apenas ativos")
    print("5 - Listar apenas inativos")
    print("0 - Voltar")
    return input("\nEscolha uma opção de listagem: ")

def display_emprestimos_ativos(emprestimos: List[Any]) -> None:
    """
    Exibe uma lista de empréstimos ativos no terminal de forma formatada.

    Args:
        emprestimos: Uma lista de objetos Emprestimo.
    """
    if not emprestimos:
        print("\nNenhum empréstimo ativo encontrado.")
        return

    print("\n--- Empréstimos Ativos ---")
    for emprestimo in emprestimos:
        print(f"ID do Empréstimo: {emprestimo.id}")
        print(f"  Usuário: {emprestimo.usuario.nome} (Matrícula: {emprestimo.usuario.matricula})")
        print(f"  Livro: {emprestimo.exemplar.livro.titulo} (ID do Livro: {emprestimo.exemplar.livro.livro_id})")
        print(f"  Exemplar ID: {emprestimo.exemplar_id}")
        data_emprestimo_str = emprestimo.data_emprestimo.strftime('%d/%m/%Y %H:%M') if emprestimo.data_emprestimo else 'N/A'
        data_devolucao_prevista_str = emprestimo.data_devolucao_prevista.strftime('%d/%m/%Y') if emprestimo.data_devolucao_prevista else 'N/A'

        print(f"  Data do Empréstimo: {data_emprestimo_str}")
        print(f"  Data de Devolução Prevista: {data_devolucao_prevista_str}")
        print("-" * 30)

def display_historico_emprestimos(usuario: Usuario, historico: List[Any]) -> None:
    """
    Exibe o histórico de empréstimos de um usuário.

    Args:
        usuario: O objeto do usuário cujo histórico está sendo exibido.
        historico: Uma lista de objetos Emprestimo.
    """
    print(f"\n--- Histórico de Empréstimos do Usuário: {usuario.nome} (ID: {usuario.id}) ---")

    if not historico:
        print("Nenhum empréstimo encontrado para este usuário.")
        return

    for emprestimo in historico:
        status = "Devolvido"
        if emprestimo.data_devolucao_efetiva is None:
            if emprestimo.data_devolucao_prevista and emprestimo.data_devolucao_prevista < date.today():
                status = "Atrasado"
            else:
                status = "Ativo"

        print(f"ID do Empréstimo: {emprestimo.id}")
        if hasattr(emprestimo, 'exemplar') and emprestimo.exemplar and hasattr(emprestimo.exemplar, 'livro') and emprestimo.exemplar.livro:
            print(f"  Livro: {emprestimo.exemplar.livro.titulo}")
        else:
            print(f"  Livro: (Informação do livro indisponível)")

        print(f"  Exemplar ID: {emprestimo.exemplar_id}")
        
        data_emprestimo_str = emprestimo.data_emprestimo.strftime('%d/%m/%Y %H:%M') if emprestimo.data_emprestimo and isinstance(emprestimo.data_emprestimo, (datetime, date)) else 'N/A'
        data_devolucao_prevista_str = emprestimo.data_devolucao_prevista.strftime('%d/%m/%Y') if emprestimo.data_devolucao_prevista and isinstance(emprestimo.data_devolucao_prevista, (datetime, date)) else 'N/A'
        data_devolucao_efetiva_str = emprestimo.data_devolucao_efetiva.strftime('%d/%m/%Y') if emprestimo.data_devolucao_efetiva and isinstance(emprestimo.data_devolucao_efetiva, (datetime, date)) else 'N/A'

        print(f"  Data do Empréstimo: {data_emprestimo_str}")
        print(f"  Data de Devolução Prevista: {data_devolucao_prevista_str}")
        print(f"  Data de Devolução Efetiva: {data_devolucao_efetiva_str}")
        print(f"  Status: {status}")
        print("-" * 30)

def get_nova_senha() -> str:
    """
    Solicita ao administrador a nova senha para um usuário.

    Returns:
        A nova senha inserida.
    """
    print("\n--- Redefinição de Senha ---")
    return input("Digite a nova senha: ")

def show_senha_redefinida(usuario: Usuario):
    """
    Exibe uma mensagem de sucesso após a redefinição da senha.
    """
    print(f"\nA senha do usuário '{usuario.nome}' (ID: {usuario.id}) foi redefinida com sucesso!")

