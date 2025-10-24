import os
from controllers.livro_controller import LivroController
from controllers.exemplar_controller import ExemplarController
from controllers.usuario_controller import UsuarioController
from controllers.administrador_controller import AdministradorController
from views.main_view import menu_admin, menu_leitor

def clear_screen():
    """Limpa a tela do terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_gestao_livros():
    """Exibe o submenu de gestão de livros e gerencia as ações."""
    controller = LivroController()

    while True:
        clear_screen()
        print("======== GERENCIAR LIVROS ========")
        print("1 - Listar todos os livros do acervo")
        print("2 - Cadastrar novo livro")
        print("3 - Editar informações de um livro")
        print("4 - Excluir livro do acervo")
        print("0 - Voltar")
        print("-----------------------------------")
        
        escolha = input("Digite o número da opção desejada: ")

        if escolha == '1':
            controller.listar_livros()
        elif escolha == '2':
            controller.adicionar_livro()
        elif escolha == '3':
            controller.atualizar_livro()
        elif escolha == '4':
            controller.deletar_livro()
        elif escolha == '0':
            break
        else:
            print("Opção inválida!")
        
        input("\nPressione Enter para continuar...")

def menu_gestao_exemplares():
    """Exibe o submenu de gestão de exemplares e gerencia as ações."""
    controller = ExemplarController()

    while True:
        clear_screen()
        print("====== GERENCIAR EXEMPLARES ======")
        print("1 - Listar exemplares disponíveis")
        print("2 - Adicionar novo exemplar")
        print("3 - Editar exemplar existente")
        print("4 - Excluir exemplar")
        print("0 - Voltar")
        print("-----------------------------------")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == '1':
            controller.listar_exemplares()
        elif escolha == '2':
            controller.adicionar_exemplar()
        elif escolha == '3':
            controller.atualizar_exemplar()
        elif escolha == '4':
            controller.deletar_exemplar()
        elif escolha == '0':
            break
        else:
            print("Opção inválida!")

        input("\nPressione Enter para continuar...")

def menu_gestao_usuarios():
    """Exibe o submenu de gestão de usuários e gerencia as ações."""
    controller = AdministradorController()

    while True:
        clear_screen()
        print("====== GERENCIAR USUÁRIOS ======")
        print("1 - Listar todos os usuários")
        print("2 - Cadastrar novo usuário")
        print("3 - Editar informações de um usuário")
        print("4 - Excluir usuário")
        print("0 - Voltar")
        print("-----------------------------------")
        
        escolha = input("Digite o número da opção desejada: ")

        if escolha == '1':
            controller.listar_usuarios()
        elif escolha == '2':
            controller.adicionar_usuario()
        elif escolha == '3':
            controller.atualizar_usuario()
        elif escolha == '4':
            controller.deletar_usuario()
        elif escolha == '0':
            break
        else:
            print("Opção inválida!")
        
        input("\nPressione Enter para continuar...")


def main():
    """Função principal que exibe o menu inicial e gerencia a navegação."""
    usuario_controller = UsuarioController()
    exemplar_controller = ExemplarController()
    usuario_logado = None

    while True:
        if not usuario_logado:
            clear_screen()
            print("---- BookMeNow ----")
            print("- Bem-vindo ao Sistema de Gestão de Bibliotecas -")
            print("\n1 - Listar Livros Disponíveis")
            print("2 - Fazer Login")
            print("3 - Sair")

            escolha = input("\nEscolha uma opção: ")

            if escolha == '1':
                exemplar_controller.listar_exemplares_disponiveis()
                input("\nPressione Enter para continuar...")
            elif escolha == '2':
                usuario_logado = usuario_controller.login()
            elif escolha == '3':
                print("Saindo do sistema. Até logo!")
                break
            else:
                print("Opção inválida! Tente novamente.")
                input("\nPressione Enter para continuar...")
        else:
            if usuario_logado.tipo_usuario == 'administrador':
                acao = menu_admin(usuario_logado, menu_gestao_livros, menu_gestao_exemplares, menu_gestao_usuarios)
            else: # Assumindo que o outro tipo é 'leitor'
                acao = menu_leitor(usuario_logado)

            if acao == 'logout':
                usuario_logado = None
                print("Logout realizado com sucesso.")
                input("\nPressione Enter para voltar ao menu principal...")
            elif acao == 'sair':
                print("Saindo do sistema. Até logo!")
                break

if __name__ == "__main__":
    main()
