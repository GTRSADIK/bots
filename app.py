from flask import Flask, request, send_file
from PIL import Image, ImageDraw, ImageFont
import io
import time

app = Flask(__name__)

FONT_PATH = "DejaVuSans-Bold.ttf"

BACKGROUND_TEMPLATES = {
    "default": "cheque.png"
}

@app.route("/image/cheque")
def cheque():
    # Query parameters
    coin_code = request.args.get("coinCode", "USDT")
    amount_crypto = request.args.get("amountCrypto", "0.01")
    amount_fiat = request.args.get("amountFiat", "0.01")
    fiat_code = request.args.get("fiatCode", "usd")
    background_type = request.args.get("backgroundType", "default")
    version = request.args.get("v", str(int(time.time()*1000)))  # auto timestamp if not provided

    # Load template
    template_file = BACKGROUND_TEMPLATES.get(background_type, "cheque.png")
    img = Image.open(template_file).convert("RGB")
    draw = ImageDraw.Draw(img)

    # Load font
    font = ImageFont.truetype(FONT_PATH, 50)

    # Draw crypto amount
    draw.text((400, 200), f"{coin_code} {amount_crypto}", fill=(255,255,255), font=font)
    
    # Draw fiat amount
    draw.text((400, 300), f"{fiat_code.upper()} {amount_fiat}", fill=(255,255,255), font=font)
    
    # Save to memory
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)

    return send_file(buf, mimetype="image/png")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
