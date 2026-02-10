import os
from flask import Flask, request, send_file
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)

PORT = int(os.environ.get("PORT", 8080))  # Railway port
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # ensure paths correct

@app.route("/cheque")
def cheque():
    coinCode = request.args.get("coinCode", "USDT")
    amountCrypto = request.args.get("amountCrypto", "0.01")
    amountFiat = request.args.get("amountFiat", "0.01")
    
    # Image path
    img_path = os.path.join(BASE_DIR, "cheque.png")
    font_path = os.path.join(BASE_DIR, "DejaVuSans-Bold.ttf")

    # Load image
    img = Image.open(img_path)
    draw = ImageDraw.Draw(img)

    # Load font
    font = ImageFont.truetype(font_path, 48)

    # Write text
    draw.text((500, 300), f"{amountCrypto} {coinCode}", font=font, fill=(0, 0, 0))
    draw.text((500, 400), f"${amountFiat}", font=font, fill=(0, 0, 255))

    # Save temp
    temp_path = os.path.join(BASE_DIR, "cheque_temp.png")
    img.save(temp_path)

    return send_file(temp_path, mimetype="image/png")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
