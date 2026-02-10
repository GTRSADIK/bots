from flask import Flask, redirect, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Cheque Generator API is running ✅"

@app.route("/cheque")
def cheque():
    coin = request.args.get("coinCode", "USDT")
    amount_crypto = request.args.get("amountCrypto", "0.01")
    amount_fiat = request.args.get("amountFiat", amount_crypto)
    background = request.args.get("backgroundType", "default")

    # Redirect to Xrocket API
    url = f"https://image.api.xrocket.tg/image/cheque?coinCode={coin}&amountCrypto={amount_crypto}&backgroundType={background}&amountFiat={amount_fiat}&fiatCode=USD"
    return redirect(url, code=302)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
