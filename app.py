from flask import Flask, request, send_file
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)

@app.route("/cheque")
def cheque():
    coinCode = request.args.get("coinCode", "USDT")
    amountCrypto = request.args.get("amountCrypto", "0.01")
    amountFiat = request.args.get("amountFiat", "0.01")
    backgroundType = request.args.get("backgroundType", "default")

    # Load base image
    img = Image.open("bots/cheque.png")
    draw = ImageDraw.Draw(img)

    # Load font
    font = ImageFont.truetype("bots/DejaVuSans-Bold.ttf", 48)

    # Write the amount text
    draw.text((500, 300), f"{amountCrypto} {coinCode}", font=font, fill=(0, 0, 0))
    draw.text((500, 400), f"${amountFiat}", font=font, fill=(0, 0, 255))  # blue for fiat

    # Save temp
    img.save("bots/cheque_temp.png")

    return send_file("bots/cheque_temp.png", mimetype="image/png")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
