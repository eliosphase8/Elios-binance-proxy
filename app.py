 from flask import Flask, jsonify
from binance.client import Client
import os

app = Flask(__name__)

client = Client(os.getenv("BINANCE_API_KEY"), os.getenv("BINANCE_SECRET_KEY"))

@app.route("/")
def home():
    return {"status": "Binance Proxy actif"}

@app.route("/balance", methods=["GET"])
def get_balance():
    try:
        account = client.get_account()
        balances = {b["asset"]: b["free"] for b in account["balances"] if float(b["free"]) > 0}
        return jsonify(balances)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
