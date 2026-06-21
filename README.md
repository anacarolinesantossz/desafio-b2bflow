# Desafio b2bflow

Automação para integração entre Supabase e Z-API.

## 1. Variáveis de Ambiente
Crie um arquivo `.env` na raiz do projeto (baseado no `.env.example`) e configure:
* `SUPABASE_URL`
* `SUPABASE_KEY`
* `ZAPI_INSTANCE`
* `ZAPI_TOKEN`

## 2. Setup do Banco (Supabase)
Crie uma tabela chamada `contatos` com as colunas:
* `nome` (text)
* `telefone` (text)

*Nota: Certifique-se de habilitar o acesso `SELECT` para a role `anon` nas políticas (RLS) da tabela.*

## 3. Como rodar
Instale as dependências:
```bash
pip install supabase requests python-dotenv

python main.py
