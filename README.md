# Projeto BookMeNow - Gerado com Google Gemini

**Gerado em:** 18 de setembro de 2025

## Sobre o Projeto

**BookMeNow** é uma aplicação de linha de comando (CLI) para gerenciamento de bibliotecas. O sistema foi projetado para lidar com o cadastro de livros, exemplares, usuários e o controle de empréstimos.

A estrutura inicial, a modelagem de classes ORM, a arquitetura MVC e o código boilerplate deste projeto foram gerados através de uma série de prompts para o Google Gemini, utilizando um DDL (Data Definition Language) como base para a modelagem do banco de dados no Supabase.

## Tecnologias Utilizadas

*   **Linguagem:** Python 3.9+
*   **Backend & Banco de Dados:** Supabase (PostgreSQL)
*   **Biblioteca de Cliente:** `supabase-py` para comunicação com o Supabase.
*   **Gerenciamento de Configuração:** `python-dotenv`

## Arquitetura

A aplicação foi desenvolvida seguindo padrões de arquitetura modernos para garantir organização, manutenibilidade e escalabilidade.

### MVC (Model-View-Controller)

*   **Model:** A camada de dados, implementada como um ORM (Active Record). As classes em `models/` representam as tabelas do banco de dados e contêm a lógica de persistência.
*   **View:** A camada de apresentação. São os módulos em `views/` responsáveis por toda a interação com o usuário no terminal (exibir menus, solicitar dados, etc.).
*   **Controller:** A camada de lógica de negócio. Os módulos em `controllers/` orquestram o fluxo da aplicação, respondendo às ações do usuário (vindas da View) e manipulando os dados (através do Model).

### ORM (Padrão Active Record)

As classes de modelo herdam de uma `BaseModel`, que lhes dá a capacidade de se auto-gerenciarem no banco de dados. Isso significa que um objeto de uma classe como `Livro` pode ser salvo, atualizado ou deletado usando seus próprios métodos, como `livro.save()` e `livro.delete()`.

## Como Configurar o Ambiente

Siga os passos abaixo para configurar e executar o projeto em sua máquina local.

**1. Clone o Repositório**

```bash
git clone <URL_DO_SEU_REPOSITORIO>
cd <NOME_DO_REPOSITORIO>
```

**2. Crie e Ative um Ambiente Virtual (Recomendado)**

*   No macOS/Linux:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
*   No Windows:
    ```bash
    py -m venv venv
    venv\Scripts\activate
    ```

**3. Instale as Dependências**
Execute o comando abaixo para instalar as bibliotecas necessárias:

```bash
pip install -r requirements.txt
```

**4. Configure o Banco de Dados no Supabase**

*   Crie um novo projeto no seu painel do [Supabase](https://supabase.com).
*   Vá para a seção **"SQL Editor"**.
*   Copie e execute o script SQL do DDL para criar as tabelas `livros`, `usuarios`, `exemplares` e `emprestimos`.

**5. Configure as Credenciais**

*   No seu projeto Supabase, vá em **Project Settings -> API**.
*   Copie a **URL** e a chave **`service_role`**.
*   Na raiz do projeto (`BMN/`), crie um arquivo chamado `.env`.
*   Adicione suas credenciais ao arquivo `.env` da seguinte forma:

```
SUPABASE_URL="SUA_URL_AQUI"
SUPABASE_KEY="SUA_CHAVE_DE_SERVICO_AQUI"
```

## Como Executar a Aplicação

Com o ambiente virtual ativado e as dependências instaladas, navegue até o diretório da aplicação e execute o comando:

```bash
cd bookmenow
python main.py
```

O menu principal da aplicação será exibido no terminal, e você poderá começar a interagir com o sistema.

## Próximos Passos

*   Implementar a lógica completa para a gestão de **Exemplares** (listar, atualizar, deletar).
*   Desenvolver as funcionalidades de CRUD para **Usuários** (Leitores e Administradores).
*   Criar a lógica de negócio para realizar e registrar a devolução de **Empréstimos**.
*   Implementar lógica de login para diferentes tipos de Usuários.
*   Adicionar validação de dados de entrada e tratamento de erros mais robusto em todas as seções.
