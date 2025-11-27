class UsuarioView:

    def solicitar_dados_login(self):
        print("--- Login ---")
        identificador = input("Digite seu e--mail ou matrícula: ")
        senha = input("Digite sua senha: ")
        return {"identificador": identificador, "senha": senha}

    def solicitar_nova_senha(self):
        print("--- Alterar Senha ---")
        senha_atual = input("Digite sua senha atual: ")
        nova_senha = input("Digite sua nova senha: ")
        confirmacao_nova_senha = input("Confirme sua nova senha: ")
        return {
            "senha_atual": senha_atual,
            "nova_senha": nova_senha,
            "confirmacao_nova_senha": confirmacao_nova_senha,
        }

    def exibir_mensagem(self, mensagem):
        print(f"{mensagem}")
        input("Pressione Enter para continuar...")
