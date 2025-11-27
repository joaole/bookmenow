import bcrypt
import os
import datetime
from dotenv import load_dotenv
from models.usuario import Usuario
from views import administrador_view

load_dotenv()


class AdministradorController:
    """
    Controlador para a gestão de usuários por administradores.
    """

    def _hash_password(self, password: str) -> str:
        """Gera o hash de uma senha usando bcrypt."""
        rounds = int(os.getenv("BCRYPT_ROUNDS", 12))
        salt = bcrypt.gensalt(rounds=rounds)
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
        return hashed_password.decode("utf-8")

    def _gerar_nova_matricula(self) -> int:
        """
        Gera uma nova matrícula com base no ano atual e na última matrícula cadastrada.
        """
        ano_atual = datetime.date.today().year
        max_matricula = Usuario.get_max_matricula_for_year(ano_atual)

        if max_matricula:
            return max_matricula + 1
        else:
            return int(f"{ano_atual}001")

    def adicionar_usuario(self):
        """
        Orquestra o processo de adicionar um novo usuário com matrícula automática.
        """
        try:
            nova_matricula = self._gerar_nova_matricula()
            print(f"A matrícula do novo usuário será: {nova_matricula}")

            dados_usuario = administrador_view.get_usuario_info()
            dados_usuario["matricula"] = nova_matricula

            if not all(
                [
                    dados_usuario.get("nome"),
                    dados_usuario.get("email"),
                    dados_usuario.get("senha"),
                ]
            ):
                print("Nome, email e senha são obrigatórios!")
                return

            dados_usuario["senha_hash"] = self._hash_password(
                dados_usuario.pop("senha")
            )

            tipo = dados_usuario.get("tipo_usuario")
            if tipo == "leitor":
                from models.usuario import Leitor

                usuario = Leitor(**dados_usuario)
            elif tipo == "administrador":
                from models.usuario import Administrador

                usuario = Administrador(**dados_usuario)
            else:
                print("Tipo de usuário inválido.")
                return

            usuario.save()
            administrador_view.show_usuario_criado(usuario)
        except Exception as e:
            print(f"Erro ao criar usuário: {e}")

    def listar_usuarios(self):
        """
        Orquestra a listagem de usuários com base em filtros.
        """
        while True:
            escolha = administrador_view.menu_listar_usuarios()
            filtro = {}

            if escolha == "1":
                # Listar todos
                pass
            elif escolha == "2":
                filtro = {"tipo_usuario": "administrador"}
            elif escolha == "3":
                filtro = {"tipo_usuario": "leitor"}
            elif escolha == "4":
                filtro = {"ativo": True}
            elif escolha == "5":
                filtro = {"ativo": False}
            elif escolha == "0":
                break
            else:
                print("Opção inválida!")
                continue

            try:
                usuarios = Usuario.find_by(filtro)
                administrador_view.display_usuarios(usuarios)
            except Exception as e:
                print(f"Erro ao listar usuários: {e}")

            input("Pressione Enter para continuar...")

    def listar_emprestimos_ativos(self):
        """
        Orquestra a listagem de todos os empréstimos ativos.
        """
        try:
            from models.emprestimo import (
                Emprestimo,
            )  # Import inside the method to avoid circular dependency

            emprestimos_ativos = Emprestimo.find_all_active_loans()
            administrador_view.display_emprestimos_ativos(emprestimos_ativos)
        except Exception as e:
            print(f"Erro ao listar empréstimos ativos: {e}")

    def _simple_list_usuarios(self):
        """Busca e exibe todos os usuários, retornando a lista."""
        try:
            usuarios = Usuario.find_all()
            administrador_view.display_usuarios(usuarios)
            return usuarios
        except Exception as e:
            print(f"Erro ao listar usuários: {e}")
            return []

    def atualizar_usuario(self):
        """
        Orquestra a atualização de um usuário existente.
        """
        usuarios = self._simple_list_usuarios()
        if not usuarios:
            return

        usuario_id = administrador_view.get_usuario_id_para_operacao("atualizar")
        usuario = Usuario.find_by_id(usuario_id)

        if not usuario:
            print("Usuário não encontrado!")
            return

        novos_dados = administrador_view.get_dados_atualizacao_usuario(usuario)

        # Atualiza os atributos do objeto usuario
        usuario.nome = novos_dados["nome"]
        usuario.email = novos_dados["email"]
        usuario.telefone = novos_dados["telefone"]
        usuario.endereco = novos_dados["endereco"]
        usuario.cargo = novos_dados["cargo"]
        usuario.ativo = novos_dados["ativo"]

        try:
            usuario.save()  # O método save() fará o UPDATE
            administrador_view.show_usuario_atualizado(usuario)
        except Exception as e:
            print(f"Erro ao atualizar usuário: {e}")

    def deletar_usuario(self):
        """
        Orquestra a desativação de um usuário (soft delete).
        """
        usuarios = self._simple_list_usuarios()
        if not usuarios:
            return

        usuario_id = administrador_view.get_usuario_id_para_operacao("desativar")
        usuario = Usuario.find_by_id(usuario_id)

        if not usuario:
            print("Usuário não encontrado!")
            return

        try:
            usuario.ativo = False
            usuario.save()
            administrador_view.show_usuario_desativado(usuario_id)
        except Exception as e:
            print(f"Erro ao desativar usuário: {e}")

    def consultar_historico_usuario(self):
        """
        Orquestra a consulta do histórico de empréstimos de um usuário específico.
        """
        try:
            # Primeiro, lista os usuários para o admin saber qual ID usar
            usuarios = self._simple_list_usuarios()
            if not usuarios:
                return

            usuario_id = administrador_view.get_usuario_id_para_operacao(
                "consultar o histórico"
            )
            usuario = Usuario.find_by_id(usuario_id)

            if not usuario:
                print("\nUsuário não encontrado!")
                return

            from models.emprestimo import Emprestimo

            historico = Emprestimo.find_history_by_user(usuario_id)
            administrador_view.display_historico_emprestimos(usuario, historico)

        except Exception as e:
            print(f"\nErro ao consultar histórico: {e}")

    def redefinir_senha_usuario(self):
        """
        Orquestra a redefinição da senha de um usuário pelo administrador.
        """
        try:
            usuarios = self._simple_list_usuarios()
            if not usuarios:
                return

            usuario_id = administrador_view.get_usuario_id_para_operacao(
                "redefinir a senha"
            )
            usuario = Usuario.find_by_id(usuario_id)

            if not usuario:
                print("\nUsuário não encontrado!")
                return

            nova_senha = administrador_view.get_nova_senha()
            if not nova_senha:
                print("\nA senha não pode estar em branco.")
                return

            nova_senha_hash = self._hash_password(nova_senha)
            usuario.senha_hash = nova_senha_hash

            usuario.save()
            administrador_view.show_senha_redefinida(usuario)

        except Exception as e:
            print(f"\nErro ao redefinir a senha: {e}")
