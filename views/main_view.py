import os

def clear_screen():
    """Limpa a tela do terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_leitor(usuario, usuario_controller, livro_controller, emprestimo_controller):
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
            livro_controller.listar_livros()
        elif escolha == '2':
            livro_controller.buscar_livro_por_titulo()
        elif escolha == '3':
            livro_controller.buscar_livro_por_autor()
        elif escolha == '4':
            emprestimo_controller.listar_emprestimos_ativos(usuario)
        elif escolha == '5':
            emprestimo_controller.listar_historico_emprestimos(usuario)
        elif escolha == '6':
            usuario_controller.alterar_senha(usuario)
        elif escolha == '7':
            print("\nSaindo...")
            return 'logout'
        elif escolha == '0':
            return 'sair'
        else:
            print("\nOpção inválida! Tente novamente.")
        
        input("\nPressione Enter para continuar...")

def menu_gestao_emprestimos(emprestimo_controller):
    """Exibe o submenu de gestão de empréstimos e gerencia as ações."""
    while True:
        clear_screen()
        print("====== GERENCIAR EMPRÉSTIMOS ======")
        print("1 - Registrar novo empréstimo")
        print("2 - Registrar devolução")
        print("0 - Voltar")
        print("-----------------------------------")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == '1':
            emprestimo_controller.registrar_emprestimo()
        elif escolha == '2':
            emprestimo_controller.registrar_devolucao()
        elif escolha == '0':
            break
        else:
            print("Opção inválida!")
        
        input("\nPressione Enter para continuar...")

def menu_admin(usuario, usuario_controller, administrador_controller, menu_gestao_livros, menu_gestao_exemplares, menu_gestao_usuarios, menu_gestao_emprestimos):
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
        print("7 - Redefinir senha de um usuário")
        print("8 - Alterar minha própria senha")
        print("9 - Realizar logout")
        print("----------------------------------------")
        print("0 - Sair do sistema")
        print("----------------------------------------")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == '1':
            menu_gestao_livros()
        elif escolha == '2':
            menu_gestao_exemplares()
        elif escolha == '3':
            menu_gestao_usuarios()
        elif escolha == '4':
            menu_gestao_emprestimos()
        elif escolha == '5':
            print("\n[Consultar histórico de um usuário] em desenvolvimento...")
        elif escolha == '6':
            administrador_controller.listar_emprestimos_ativos()
        elif escolha == '7':
            print("\n[Redefinir senha de um usuário] em desenvolvimento...")
        elif escolha == '8':
            usuario_controller.alterar_senha(usuario)
        elif escolha == '9':
            print("\nSaindo...")
            return 'logout'
        elif escolha == '0':
            return 'sair'
        else:
            print("\nOpção inválida! Tente novamente.")

        if escolha not in ['1', '2']:
            input("\nPressione Enter para continuar...")
