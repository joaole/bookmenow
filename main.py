import os
from controllers.livro_controller import LivroController
from controllers.exemplar_controller import ExemplarController

def clear_screen():
    """Limpa a tela do terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_gestao_livros():
    """Exibe o submenu de gestão de livros e gerencia as ações."""
    controller = LivroController()

    while True:
        clear_screen()
        print("--- Gestão de Livros ---")
        print("1 - Cadastrar Novo Livro")
        print("2 - Listar Todos os Livros")
        print("3 - Atualizar Livro")
        print("4 - Deletar Livro")
        print("5 - Voltar ao Menu Principal")
        
        escolha = input("\nEscolha uma opção: ")

        if escolha == '1':
            controller.adicionar_livro()
        elif escolha == '2':
            controller.listar_livros()
        elif escolha == '3':
            controller.atualizar_livro()
        elif escolha == '4':
            controller.deletar_livro()
        elif escolha == '5':
            break
        else:
            print("Opção inválida!")
        
        input("\nPressione Enter para continuar...")

def menu_gestao_exemplares():
    """Exibe o submenu de gestão de exemplares e gerencia as ações."""
    controller = ExemplarController()

    while True:
        clear_screen()
        print("--- Gestão de Exemplares ---")
        print("1 - Cadastrar Novo Exemplar")
        print("2 - Voltar ao Menu Principal")

        escolha = input("\nEscolha uma opção: ")

        if escolha == '1':
            controller.adicionar_exemplar()
        elif escolha == '2':
            break
        else:
            print("Opção inválida!")

        input("\nPressione Enter para continuar...")

def main():
    """Função principal que exibe o menu principal e gerencia a navegação."""
    while True:
        clear_screen()
        print("---- BookMeNow ----")
        print("- Sistema de Gestão de Bibliotecas -")
        print("\n1 - Gestão de Livros")
        print("2 - Gestão de Exemplares")
        print("3 - Sair")

        escolha = input("\nEscolha uma opção: ")

        if escolha == '1':
            menu_gestao_livros()
        elif escolha == '2':
            menu_gestao_exemplares()
        elif escolha == '3':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")
            input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()
