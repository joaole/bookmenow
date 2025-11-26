
from abc import ABC, abstractmethod
from typing import List, TypeVar, Type, Dict, Any
from config import supabase_client

# Genérico para representar uma instância de uma subclasse de BaseModel
T = TypeVar('T', bound='BaseModel')

class BaseModel(ABC):
    """
    Classe base abstrata para o ORM (Active Record).

    Fornece métodos CRUD básicos que interagem com o Supabase.
    As classes de modelo concretas devem herdar desta classe e definir
    a propriedade 'table_name'.
    """

    # O nome da tabela no Supabase. Deve ser sobrescrito pelas subclasses.
    table_name: str = ""
    # O nome da chave primária. Pode ser sobrescrito se não for 'id'.
    primary_key: str = "id"

    def __init__(self, **kwargs):
        """
        Inicializa o objeto do modelo com os dados passados.
        Os nomes dos argumentos devem corresponder às colunas da tabela.
        """
        for key, value in kwargs.items():
            setattr(self, f"_{key}", value)

    def to_dict(self) -> Dict[str, Any]:
        """
        Converte o objeto em um dicionário, removendo o sublinhado dos nomes dos atributos.
        """
        return {key.lstrip('_'): value for key, value in self.__dict__.items() if key.startswith('_')}

    def save(self) -> None:
        """
        Salva (insere ou atualiza) o registro no banco de dados.

        Se o objeto já tem um ID (chave primária), ele executa um UPDATE.
        Caso contrário, executa um INSERT.
        """
        # Converte o objeto em um dicionário para o Supabase
        data = self.to_dict()
        pk_value = getattr(self, f"_{self.primary_key}", None)

        try:
            if pk_value:
                # UPDATE: Atualiza o registro existente
                # Cria uma cópia dos dados para não modificar o objeto original
                update_data = data.copy()
                # Remove a chave primária do dicionário para evitar tentar atualizá-la               
                if self.primary_key in update_data:
                    del update_data[self.primary_key]
                query = supabase_client.table(self.table_name).update(update_data)
                query = query.eq(self.primary_key, pk_value)
                result = query.execute()
            else:
                # INSERT: Insere um novo registro
                # Cria uma cópia dos dados para não modificar o objeto original
                insert_data = data.copy()
                # Remove a chave primária do dicionário se ela for None,
                # para que o banco de dados possa gerá-la automaticamente.
                if insert_data.get(self.primary_key) is None:
                    del insert_data[self.primary_key]
                
                result = supabase_client.table(self.table_name).insert(insert_data).execute()
            
            # Após a inserção, o Supabase retorna os dados do novo registro.
            # Atualizamos o objeto com o ID gerado pelo banco.
            if not pk_value and result.data:
                new_data = result.data[0]
                for key, value in new_data.items():
                    setattr(self, key, value)

        except Exception as e:
            print(f"Erro ao salvar no banco de dados ({self.table_name}): {e}")

    def delete(self) -> None:
        """
        Deleta o registro correspondente do banco de dados.
        """
        pk_value = getattr(self, f"_{self.primary_key}", None)
        if not pk_value:
            print("Erro: Não é possível deletar um objeto que ainda não foi salvo.")
            return

        try:
            supabase_client.table(self.table_name).delete().eq(self.primary_key, pk_value).execute()
        except Exception as e:
            print(f"Erro ao deletar no banco de dados ({self.table_name}): {e}")

    @classmethod
    def find_by_id(cls: Type[T], pk_value: Any) -> T | None:
        """
        Busca um único registro pela sua chave primária.

        Args:
            pk_value: O valor da chave primária a ser buscada.

        Returns:
            Uma instância da classe do modelo se encontrado, caso contrário None.
        """
        try:
            result = supabase_client.table(cls.table_name).select("*").eq(cls.primary_key, pk_value).execute()
            if result.data:
                data = result.data[0]
                # Tratamento para Herança de Tabela Única (Single-Table Inheritance)
                if cls.__name__ == 'Usuario' and 'tipo_usuario' in data:
                    from models.usuario import Leitor, Administrador
                    if data['tipo_usuario'] == 'leitor':
                        return Leitor(**data)
                    elif data['tipo_usuario'] == 'administrador':
                        return Administrador(**data)
                return cls(**data) # Fallback for other classes
            return None
        except Exception as e:
            print(f"Erro ao buscar por ID na tabela {cls.table_name}: {e}")
            return None

    @classmethod
    def find_all(cls: Type[T]) -> List[T]:
        """
        Busca todos os registros de uma tabela.

        Returns:
            Uma lista de instâncias da classe do modelo.
        """
        try:
            result = supabase_client.table(cls.table_name).select("*").execute()
            if result.data:
                instances = []
                # Tratamento para Herança de Tabela Única (Single-Table Inheritance)
                if cls.__name__ == 'Usuario':
                    from models.usuario import Leitor, Administrador
                    for item in result.data:
                        if item.get('tipo_usuario') == 'leitor':
                            instances.append(Leitor(**item))
                        elif item.get('tipo_usuario') == 'administrador':
                            instances.append(Administrador(**item))
                        else:
                            # Caso o tipo não seja especificado ou seja inválido,
                            # pode-se optar por não instanciar ou lançar um erro.
                            # Aqui, simplesmente ignoramos.
                            pass
                    return instances
                else:
                    # Comportamento padrão para outras classes
                    return [cls(**item) for item in result.data]
            return []
        except Exception as e:
            print(f"Erro ao buscar todos os registros na tabela {cls.table_name}: {e}")
            return []

    @classmethod
    def find_by(cls: Type[T], filters: Dict[str, Any]) -> List[T]:
        """
        Busca registros com base em um ou mais filtros.

        Args:
            filters: Dicionário com os pares de chave-valor para filtrar a busca.

        Returns:
            Uma lista de instâncias da classe do modelo.
        """
        try:
            query = supabase_client.table(cls.table_name).select("*")
            for key, value in filters.items():
                query = query.eq(key, value)
            
            result = query.execute()

            if result.data:
                instances = []
                # Tratamento para Herança de Tabela Única (Single-Table Inheritance)
                if cls.__name__ == 'Usuario':
                    from models.usuario import Leitor, Administrador
                    for item in result.data:
                        if item.get('tipo_usuario') == 'leitor':
                            instances.append(Leitor(**item))
                        elif item.get('tipo_usuario') == 'administrador':
                            instances.append(Administrador(**item))
                        else:
                            pass
                    return instances
                else:
                    return [cls(**item) for item in result.data]
            return []
        except Exception as e:
            print(f"Erro ao buscar registros na tabela {cls.table_name}: {e}")
            return []

    @classmethod
    def find(cls: Type[T], **kwargs) -> T | None:
        """
        Busca um único registro com base em um ou mais filtros.

        Args:
            **kwargs: Pares de chave-valor para filtrar a busca.

        Returns:
            Uma instância da classe do modelo se encontrado, caso contrário None.
        """
        try:
            query = supabase_client.table(cls.table_name).select("*")
            for key, value in kwargs.items():
                query = query.eq(key, value)
            
            result = query.limit(1).execute()
            
            if result.data:
                data = result.data[0]
                # Tratamento para Herança de Tabela Única (Single-Table Inheritance)
                if cls.__name__ == 'Usuario' and 'tipo_usuario' in data:
                    from models.usuario import Leitor, Administrador
                    if data['tipo_usuario'] == 'leitor':
                        return Leitor(**data)
                    elif data['tipo_usuario'] == 'administrador':
                        return Administrador(**data)
                return cls(**data)
            return None
        except Exception as e:
            print(f"Erro ao buscar na tabela {cls.table_name}: {e}")
            return None

    def __repr__(self) -> str:
        """
        Representação em string do objeto, útil para debugging.
        """
        attrs = ", ".join(f"{k}={v!r}" for k, v in self.to_dict().items())
        return f"<{self.__class__.__name__}({attrs})>"

    @classmethod
    def get_query(cls):
        """
        Retorna um objeto de query base para a tabela da classe.
        """
        return supabase_client.table(cls.table_name).select("*")
