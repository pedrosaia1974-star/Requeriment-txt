from flask import Flask, request, jsonify
from ai import gerar_resposta

app = Flask(__name__)

@app.route("/")
def home():
    return "JARVIS ONLINE"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    print("📩 Evento:", data)

    if data.get("status") == "APPROVED":
        cliente = data.get("data", {}).get("buyer", {}).get("name", "Cliente")

        resposta = gerar_resposta(cliente)

        print(f"💰 Venda: {cliente}")
        print("📄 IA:", resposta)

    return jsonify({"ok": True})

app.run(host="0.0.0.0", port=10000)
