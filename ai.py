import requests
import os

API_KEY = os.getenv("API_KEY")

def gerar_resposta(cliente):
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

        data = {
            "contents": [
                {"parts": [{"text": f"Mensagem curta de boas-vindas para {cliente} após compra."}]}
            ]
        }

        r = requests.post(url, json=data)

        return r.json()["candidates"][0]["content"]["parts"][0]["text"]

    except:
        return f"Bem-vindo {cliente}! 🚀"
