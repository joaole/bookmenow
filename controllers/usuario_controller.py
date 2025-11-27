import bcrypt
from models.usuario import Usuario
from views.usuario_view import UsuarioView


class UsuarioController:
    def __init__(self):
        self.usuario_view = UsuarioView()

    def login(self):
        dados_login = self.usuario_view.solicitar_dados_login()
        identifier = dados_login["identificador"]
        senha = dados_login["senha"]

        user = self._find_user(identifier)

        if user and self._verify_password(senha, user.senha_hash):
            self.usuario_view.exibir_mensagem("Login bem-sucedido!")
            return user
        else:
            self.usuario_view.exibir_mensagem(
                "Falha no login. Dados incorretos, tente novamente."
            )
            return None

    def _find_user(self, identifier):
        try:
            if "@" in identifier:
                return Usuario.find(email=identifier)
            else:
                return Usuario.find(matricula=identifier)
        except Exception as e:
            self.usuario_view.exibir_mensagem(f"Erro ao buscar usuário: {e}")
            return None

    def _verify_password(self, plain_password, hashed_password):
        return bcrypt.checkpw(
            plain_password.strip().encode("utf-8"),
            hashed_password.strip().encode("utf-8"),
        )

    def alterar_senha(self, usuario_logado):
        dados_nova_senha = self.usuario_view.solicitar_nova_senha()
        senha_atual = dados_nova_senha["senha_atual"]
        nova_senha = dados_nova_senha["nova_senha"]
        confirmacao_nova_senha = dados_nova_senha["confirmacao_nova_senha"]

        if not self._verify_password(senha_atual, usuario_logado.senha_hash):
            self.usuario_view.exibir_mensagem("Senha atual incorreta.")
            return

        if nova_senha != confirmacao_nova_senha:
            self.usuario_view.exibir_mensagem("As novas senhas não coincidem.")
            return

        nova_senha_hash = bcrypt.hashpw(
            nova_senha.strip().encode("utf-8"), bcrypt.gensalt()
        )
        usuario_logado.senha_hash = nova_senha_hash.decode("utf-8")

        try:
            usuario_logado.save()
            self.usuario_view.exibir_mensagem("Senha alterada com sucesso!")
        except Exception as e:
            self.usuario_view.exibir_mensagem(f"Erro ao alterar a senha: {e}")
