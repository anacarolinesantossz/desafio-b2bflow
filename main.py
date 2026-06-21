import os
import requests
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
ZAPI_INSTANCE = os.getenv("ZAPI_INSTANCE")
ZAPI_TOKEN = os.getenv("ZAPI_TOKEN")

def enviar_whatsapp(telefone, nome):
    url = f"https://api.z-api.io/instances/{ZAPI_INSTANCE}/token/{ZAPI_TOKEN}/send-text"
    
    mensagem = f"Olá, {nome} tudo bem com você?"
    
    try:
        req = requests.post(url, json={"phone": telefone, "message": mensagem})
        req.raise_for_status()
        print(f"✅ Mensagem enviada com sucesso para {nome}!")
    except Exception as e:
        print(f"❌ Erro ao enviar para {nome}: {e}")

def main():
    print("Iniciando o envio de mensagens...")

    try:
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

        resposta = supabase.table("contatos").select("*").execute()
        contatos = resposta.data
    except Exception as e:
        print(f"Erro ao conectar no banco: {e}")
        return

    if not contatos:
        print("Nenhum contato encontrado no banco de dados.")
        return

    for contato in contatos:
        nome = contato.get("nome")
        telefone = contato.get("telefone")

        if nome and telefone:
            enviar_whatsapp(telefone, nome)
        else:
            print("Pulando contato com dados incompletos.")

if __name__ == "__main__":
    main()