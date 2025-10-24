import bcrypt
import os
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
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')

    def adicionar_usuario(self):
        """
        Orquestra o processo de adicionar um novo usuário.
        """
        dados_usuario = administrador_view.get_usuario_info()
        
        if not all([dados_usuario.get("nome"), dados_usuario.get("email"), dados_usuario.get("senha"), dados_usuario.get("matricula")]):
            print("\nNome, email, senha e matrícula são obrigatórios!")
            return

        # Criptografa a senha
        dados_usuario["senha_hash"] = self._hash_password(dados_usuario.pop("senha"))

        usuario = Usuario(**dados_usuario)
        try:
            usuario.save()
            administrador_view.show_usuario_criado(usuario)
        except Exception as e:
            print(f"\nErro ao criar usuário: {e}")

    def listar_usuarios(self):
        """
        Orquestra a listagem de todos os usuários.
        """
        usuarios = Usuario.find_all()
        administrador_view.display_usuarios(usuarios)

    def atualizar_usuario(self):
        """
        Orquestra a atualização de um usuário existente.
        """
        self.listar_usuarios()
        usuarios = Usuario.find_all()
        if not usuarios:
            return

        usuario_id = administrador_view.get_usuario_id_para_operacao("atualizar")
        usuario = Usuario.find_by_id(usuario_id)

        if not usuario:
            print("\nUsuário não encontrado!")
            return

        novos_dados = administrador_view.get_dados_atualizacao_usuario(usuario)
        
        # Atualiza os atributos do objeto usuario
        usuario.nome = novos_dados['nome']
        usuario.email = novos_dados['email']
        usuario.telefone = novos_dados['telefone']
        usuario.endereco = novos_dados['endereco']
        usuario.cargo = novos_dados['cargo']
        usuario.ativo = novos_dados['ativo']

        try:
            usuario.save() # O método save() fará o UPDATE
            administrador_view.show_usuario_atualizado(usuario)
        except Exception as e:
            print(f"\nErro ao atualizar usuário: {e}")

    def deletar_usuario(self):
        """
        Orquestra a exclusão de um usuário.
        """
        self.listar_usuarios()
        usuarios = Usuario.find_all()
        if not usuarios:
            return

        usuario_id = administrador_view.get_usuario_id_para_operacao("deletar")
        usuario = Usuario.find_by_id(usuario_id)

        if not usuario:
            print("\nUsuário não encontrado!")
            return

        try:
            usuario.delete()
            administrador_view.show_usuario_deletado(usuario_id)
        except Exception as e:
            print(f"\nErro ao deletar usuário: {e}")