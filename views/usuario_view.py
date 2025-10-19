class UsuarioView:

    def solicitar_dados_login(self):
        print("--- Login ---")
        identificador = input("Digite seu e-mail ou matrícula: ")
        senha = input("Digite sua senha: ")
        return {"identificador": identificador, "senha": senha}

    def exibir_mensagem(self, mensagem):
        print(f"{mensagem}")
        input("Pressione Enter para continuar...")

