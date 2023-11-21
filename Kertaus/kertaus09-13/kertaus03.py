from flask import Flask, request


app = Flask(__name__)


@app.route("/")
def get_root():
    return "moi"


@app.route("/norrland")
def moromoro():
    return "jag tyckkää om Lennart"


# Argumentit
# http://127.0.0.1:5500/summa?numero1=32&numero2=34
@app.route("/summa")
def summa():
    argumentit = request.args
    num1 = int(argumentit.get("num1"))
    num2 = int(argumentit.get("num2"))
    summa = num1 + num2
    return str(summa)


# Vaihtoehtoinen tapa
# http://127.0.0.1:5500/erotus/54/18
@app.route("/erotus/<num1>/<num2>")
def erotus(num1, num2):
    summa = int(num1) - int(num2)
    return str(summa)


if __name__ == "__main__":
    app.run(host="localhost", port=5500, use_reloader=True)
