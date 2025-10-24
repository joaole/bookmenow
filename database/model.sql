-- WARNING: This schema is for context only and is not meant to be run.
-- Table order and constraints may not be valid for execution.

CREATE TABLE public.emprestimos (
  id integer GENERATED ALWAYS AS IDENTITY NOT NULL,
  usuario_id integer NOT NULL,
  exemplar_id integer NOT NULL,
  data_emprestimo timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
  data_devolucao_prevista date NOT NULL,
  data_devolucao_efetiva date,
  CONSTRAINT emprestimos_pkey PRIMARY KEY (id),
  CONSTRAINT fk_usuario FOREIGN KEY (usuario_id) REFERENCES public.usuarios(id),
  CONSTRAINT fk_exemplar FOREIGN KEY (exemplar_id) REFERENCES public.exemplares(id)
);
CREATE TABLE public.exemplares (
  id integer GENERATED ALWAYS AS IDENTITY NOT NULL,
  livro_id integer NOT NULL,
  localizacao jsonb NOT NULL,
  disponivel boolean DEFAULT true,
  CONSTRAINT exemplares_pkey PRIMARY KEY (id),
  CONSTRAINT fk_livro FOREIGN KEY (livro_id) REFERENCES public.livros(livro_id)
);
CREATE TABLE public.livros (
  livro_id integer GENERATED ALWAYS AS IDENTITY NOT NULL,
  titulo character varying NOT NULL,
  autor character varying,
  editora character varying,
  ano_publicacao integer,
  CONSTRAINT livros_pkey PRIMARY KEY (livro_id)
);
CREATE TABLE public.usuarios (
  id integer GENERATED ALWAYS AS IDENTITY NOT NULL,
  nome character varying NOT NULL,
  email character varying NOT NULL UNIQUE,
  senha_hash character varying NOT NULL,
  telefone character varying NOT NULL,
  endereco text NOT NULL,
  ativo boolean NOT NULL DEFAULT true,
  data_cadastro timestamp with time zone NOT NULL DEFAULT CURRENT_TIMESTAMP,
  tipo_usuario USER-DEFINED NOT NULL CHECK (tipo_usuario::text = ANY (ARRAY['leitor'::character varying::text, 'administrador'::character varying::text])),
  matricula integer NOT NULL UNIQUE,
  cargo character varying,
  CONSTRAINT usuarios_pkey PRIMARY KEY (id)
);