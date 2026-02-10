from flask import Flask, request, send_file
from PIL import Image, ImageDraw, ImageFont
import io
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Cheque Generator API is running ✅"

@app.route("/cheque")
def cheque():
    # Query parameters
    coin = request.args.get("coinCode", "USDT")
    amount_crypto = request.args.get("amountCrypto", "0.01")
    amount_fiat = request.args.get("amountFiat", "0.01")
    background = request.args.get("backgroundType", "default")

    # Base image path
    img_path = os.path.join(os.path.dirname(__file__), "cheque.png")
    if not os.path.exists(img_path):
        return "Base image not found", 404

    img = Image.open(img_path)
    draw = ImageDraw.Draw(img)

    # Font path
    font_path = os.path.join(os.path.dirname(__file__), "DejaVuSans-Bold.ttf")
    if not os.path.exists(font_path):
        return "Font not found", 404

    font = ImageFont.truetype(font_path, 40)

    # Text to draw
    text = f"{amount_crypto} {coin}"

    # Center the text
    w, h = img.size
    text_w, text_h = draw.textsize(text, font=font)
    x = (w - text_w) // 2
    y = (h - text_h) // 2

    draw.text((x, y), text, fill="black", font=font)

    # Return as PNG
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return send_file(buf, mimetype="image/png")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
