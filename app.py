import os
from flask import Flask, request, send_file
from PIL import Image, ImageDraw, ImageFont
import io

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHEQUE_IMG = os.path.join(BASE_DIR, "cheque.png")
FONT_TTF = os.path.join(BASE_DIR, "DejaVuSans-Bold.ttf")

@app.route("/cheque")
def cheque():
    coin = request.args.get("coinCode", "USDT")
    amc = request.args.get("amountCrypto", "0.01")
    amf = request.args.get("amountFiat", "0.01")
    img = Image.open(CHEQUE_IMG).convert("RGBA")
    d = ImageDraw.Draw(img)
    f = ImageFont.truetype(FONT_TTF, 48)
    text = f"{amc} {coin}   {amf}"
    w, h = img.size
    tw, th = d.textsize(text, font=f)
    d.text(((w-tw)/2, h-th-60), text, font=f, fill="white")
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return send_file(buf, mimetype="image/png")
