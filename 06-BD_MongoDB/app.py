from flask import Flask, render_template, request
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

mongo_uri = os.getenv("MONGODB_URI")

cliente = MongoClient(mongo_uri)
app.db = cliente.ejemplo

usuarios = [usuario for usuario in app.db.usuarios.find({})]
print(usuarios)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        info_formulario = request.form.get("contenido")
        parametros = {"nombre": info_formulario}
        usuarios.append(parametros)
        app.db.usuarios.insert_one(parametros)

    return render_template("formulario.html", usuarios=usuarios)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8090, debug=True)
