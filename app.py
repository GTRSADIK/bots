import os
from flask import Flask, send_file, request
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)

# Base directory for relative paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Default cheque image and font
CHEQUE_IMG = os.path.join(BASE_DIR, "cheque.png")
FONT_TTF = os.path.join(BASE_DIR, "DejaVuSans-Bold.ttf")

@app.route("/cheque")
def cheque():
    # Get query params
    coin_code = request.args.get("coinCode", "USDT")
    amount_crypto = request.args.get("amountCrypto", "0.01")
    amount_fiat = request.args.get("amountFiat", "0.01")
    fiat_code = request.args.get("fiatCode", "USD")
    background_type = request.args.get("backgroundType", "default")

    # Open base cheque image
    if not os.path.exists(CHEQUE_IMG):
        return "Cheque image not found", 404

    img = Image.open(CHEQUE_IMG).convert("RGBA")
    draw = ImageDraw.Draw(img)

    # Load font
    if not os.path.exists(FONT_TTF):
        return "Font file not found", 404
    font = ImageFont.truetype(FONT_TTF, 32)

    # Prepare text
    text = f"{amount_crypto} {coin_code}  |  {amount_fiat} {fiat_code}"

    # Calculate position (bottom center)
    w, h = img.size
    text_w, text_h = draw.textsize(text, font=font)
    x = (w - text_w) / 2
    y = h - text_h - 50

    # Draw text
    draw.text((x, y), text, font=font, fill="white")  # white text on default background

    # Save temp file
    temp_path = os.path.join(BASE_DIR, "temp_cheque.png")
    img.save(temp_path)

    return send_file(temp_path, mimetype="image/png")

# Railway uses PORT env
PORT = int(os.environ.get("PORT", 5000))
HOST = "0.0.0.0"

if __name__ == "__main__":
    print(f"Starting server on {HOST}:{PORT}")
    app.run(host=HOST, port=PORT)
