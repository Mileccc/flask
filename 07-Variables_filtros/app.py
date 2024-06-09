from flask import Flask, render_template

app = Flask(__name__)

usuarios = ["Ivan", "Pamela", "Antonio"]


@app.route("/")
def lista_usuarios():
    return render_template("index.html", users=usuarios, numero_usuarios=len(usuarios))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8090, debug=True)
