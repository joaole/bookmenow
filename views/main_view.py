import os

def clear_screen():
    """Limpa a tela do terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_leitor(usuario):
    """Exibe o menu de opções para o usuário Leitor."""
    while True:
        clear_screen()
        print("========================================")
        print("        📚 BookMeNow - Leitor")
        print("========================================")
        print(f"Usuário: {usuario.nome}")
        print("Tipo: Leitor")
        print("\nSelecione uma opção:")
        print("----------------------------------------")
        print("1 - Listar todos os livros do acervo")
        print("2 - Buscar livro por título")
        print("3 - Buscar livro por autor")
        print("4 - Visualizar meus empréstimos ativos")
        print("5 - Consultar meu histórico de empréstimos")
        print("6 - Alterar minha senha")
        print("7 - Realizar logout")
        print("----------------------------------------")
        print("0 - Sair do sistema")
        print("----------------------------------------")
        
        escolha = input("Digite o número da opção desejada: ")

        if escolha == '1':
            print("\n[Listar todos os livros do acervo] em desenvolvimento...")
        elif escolha == '2':
            print("\n[Buscar livro por título] em desenvolvimento...")
        elif escolha == '3':
            print("\n[Buscar livro por autor] em desenvolvimento...")
        elif escolha == '4':
            print("\n[Visualizar meus empréstimos ativos] em desenvolvimento...")
        elif escolha == '5':
            print("\n[Consultar meu histórico de empréstimos] em desenvolvimento...")
        elif escolha == '6':
            print("\n[Alterar minha senha] em desenvolvimento...")
        elif escolha == '7':
            print("\nSaindo...")
            return 'logout'
        elif escolha == '0':
            return 'sair'
        else:
            print("\nOpção inválida! Tente novamente.")
        
        input("\nPressione Enter para continuar...")

def menu_admin(usuario, menu_gestao_livros, menu_gestao_exemplares):
    """Exibe o menu de opções para o usuário Administrador."""
    while True:
        clear_screen()
        print("========================================")
        print("      ⚙️ BookMeNow - Administrador")
        print("========================================")
        print(f"Usuário: {usuario.nome}")
        print("Tipo: Administrador")
        print("\nSelecione uma opção:")
        print("----------------------------------------")
        print("1 - Gerenciar livros")
        print("2 - Gerenciar exemplares")
        print("3 - Gerenciar usuários")
        print("4 - Gerenciar empréstimos")
        print("5 - Consultar histórico de um usuário")
        print("6 - Listar todos os empréstimos ativos")
        print("7 - Listar todos os usuários cadastrados")
        print("8 - Redefinir senha de um usuário")
        print("9 - Alterar minha própria senha")
        print("10 - Realizar logout")
        print("----------------------------------------")
        print("0 - Sair do sistema")
        print("----------------------------------------")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == '1':
            menu_gestao_livros()
        elif escolha == '2':
            menu_gestao_exemplares()
        elif escolha == '3':
            print("\n[Gerenciar usuários] em desenvolvimento...")
        elif escolha == '4':
            print("\n[Gerenciar empréstimos] em desenvolvimento...")
        elif escolha == '5':
            print("\n[Consultar histórico de um usuário] em desenvolvimento...")
        elif escolha == '6':
            print("\n[Listar todos os empréstimos ativos] em desenvolvimento...")
        elif escolha == '7':
            print("\n[Listar todos os usuários cadastrados] em desenvolvimento...")
        elif escolha == '8':
            print("\n[Redefinir senha de um usuário] em desenvolvimento...")
        elif escolha == '9':
            print("\n[Alterar minha própria senha] em desenvolvimento...")
        elif escolha == '10':
            print("\nSaindo...")
            return 'logout'
        elif escolha == '0':
            return 'sair'
        else:
            print("\nOpção inválida! Tente novamente.")

        if escolha not in ['1', '2']:
            input("\nPressione Enter para continuar...")
