from abc import ABC, abstractmethod

from models.base_model import BaseModel

class Usuario(BaseModel, ABC):
    """
    Representa a tabela 'usuarios' e serve como base para Leitor e Administrador.
    Implementa a estratégia de Herança de Tabela Única (Single-Table Inheritance).
    """
    table_name = "usuarios"
    primary_key = "id"

    def __init__(self, nome: str, email: str, senha_hash: str, tipo_usuario: str, **kwargs):
        super().__init__(
            nome=nome,
            email=email,
            senha_hash=senha_hash,
            tipo_usuario=tipo_usuario,
            **kwargs
        )

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def senha_hash(self):
        return self._senha_hash

    @senha_hash.setter
    def senha_hash(self, value):
        self._senha_hash = value

    @property
    def tipo_usuario(self):
        return self._tipo_usuario

    @tipo_usuario.setter
    def tipo_usuario(self, value):
        self._tipo_usuario = value

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, value):
        self._telefone = value

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, value):
        self._endereco = value

    @property
    def ativo(self):
        return self._ativo

    @ativo.setter
    def ativo(self, value):
        self._ativo = value

    @property
    def data_cadastro(self):
        return self._data_cadastro

    @data_cadastro.setter
    def data_cadastro(self, value):
        self._data_cadastro = value

    @abstractmethod
    def realizar_login(self):
        pass

    @abstractmethod
    def realizar_logout(self):
        pass


class Leitor(Usuario):
    """
    Representa um usuário do tipo 'leitor'.
    """
    def __init__(self, nome: str, email: str, senha_hash: str, matricula: str, **kwargs):
        # Garante que o tipo_usuario não seja passado duas vezes
        kwargs.pop('tipo_usuario', None)
        # Chama o __init__ da classe base (Usuario) com o tipo definido
        super().__init__(nome, email, senha_hash, tipo_usuario='leitor', matricula=matricula, **kwargs)

    @property
    def matricula(self):
        return self._matricula

    @matricula.setter
    def matricula(self, value):
        self._matricula = value
        
    def realizar_login(self):
        # Lógica de login específica para Leitor
        print(f"Leitor {self.nome} realizou login.")

    def realizar_logout(self):
        # Lógica de logout específica para Leitor
        print(f"Leitor {self.nome} realizou logout.")


class Administrador(Usuario):
    """
    Representa um usuário do tipo 'administrador'.
    """
    def __init__(self, nome: str, email: str, senha_hash: str, cargo: str, **kwargs):
        # Garante que o tipo_usuario não seja passado duas vezes
        kwargs.pop('tipo_usuario', None)
        # Chama o __init__ da classe base (Usuario) com o tipo definido
        super().__init__(nome, email, senha_hash, tipo_usuario='administrador', cargo=cargo, **kwargs)

    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, value):
        self._cargo = value
        
    def realizar_login(self):
        # Lógica de login específica para Administrador
        print(f"Administrador {self.nome} realizou login.")

    def realizar_logout(self):
        # Lógica de logout específica para Administrador
        print(f"Administrador {self.nome} realizou logout.")

