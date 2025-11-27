import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# URL e Chave de Serviço do Supabase (substitua pelos seus valores ou use variáveis de ambiente)
SUPABASE_URL = os.getenv("SUPABASE_URL", "SUA_URL_AQUI")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "SUA_CHAVE_DE_SERVICO_AQUI")


def get_supabase_client() -> Client:
    """
    Inicializa e retorna o cliente do Supabase.

    As credenciais são lidas de variáveis de ambiente (SUPABASE_URL, SUPABASE_KEY)
    ou de placeholders no código.

    Returns:
        Client: Uma instância do cliente Supabase.
    """
    if SUPABASE_URL == "SUA_URL_AQUI" or SUPABASE_KEY == "SUA_CHAVE_DE_SERVICO_AQUI":
        print("AVISO: As credenciais do Supabase não foram configuradas.")
        print("Por favor, edite o arquivo 'config.py' ou crie um arquivo '.env'.")
        # Retornar um cliente "None" ou levantar uma exceção pode ser uma alternativa.
        # Por enquanto, a aplicação tentará conectar mesmo assim.

    try:
        supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
        return supabase
    except Exception as e:
        print(f"Erro ao conectar com o Supabase: {e}")
        exit(1)


# Cliente global que pode ser importado por outros módulos
supabase_client = get_supabase_client()
