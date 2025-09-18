
from models.base_model import BaseModel

class Usuario(BaseModel):
    """
    Representa a tabela 'usuarios' e serve como base para Leitor e Administrador.
    Implementa a estratégia de Herança de Tabela Única (Single-Table Inheritance).
    """
    table_name = "usuarios"
    primary_key = "id"

    def __init__(self, nome: str, email: str, senha_hash: str, tipo_usuario: str, **kwargs):
        super().__init__()
        self.id = kwargs.get('id')
        self.nome = nome
        self.email = email
        self.senha_hash = senha_hash
        self.tipo_usuario = tipo_usuario
        # Atributos comuns que podem ou não estar presentes
        self.telefone = kwargs.get('telefone')
        self.endereco = kwargs.get('endereco')
        self.ativo = kwargs.get('ativo', True)
        self.data_cadastro = kwargs.get('data_cadastro')

class Leitor(Usuario):
    """
    Representa um usuário do tipo 'leitor'.
    """
    def __init__(self, nome: str, email: str, senha_hash: str, matricula: str, **kwargs):
        # Chama o __init__ da classe base (Usuario) com o tipo definido
        super().__init__(nome, email, senha_hash, tipo_usuario='leitor', **kwargs)
        self.matricula = matricula

class Administrador(Usuario):
    """
    Representa um usuário do tipo 'administrador'.
    """
    def __init__(self, nome: str, email: str, senha_hash: str, cargo: str, **kwargs):
        # Chama o __init__ da classe base (Usuario) com o tipo definido
        super().__init__(nome, email, senha_hash, tipo_usuario='administrador', **kwargs)
        self.cargo = cargo
