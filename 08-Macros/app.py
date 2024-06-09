from flask import Flask, render_template

app = Flask(__name__)

usuarios = [("Ivan", "admin"), ("Pamela", "user"),
            ("Antonio", "user"), ("Ana", "admin")]

usuarios2 = [("Sara", "user"), ("Javi", "user"),
             ("Isaac", "user"), ("Ramon", "admin")]

usuarios3 = [("Tomas", "user"), ("Ramon", "admin"),
             ("Almudena", "user"), ("Rocio", "admin")]


@app.route("/")
def lista_usuarios():
    return render_template("index.html", users=usuarios, users2=usuarios2)


@app.route("/usuario3")
def lista_usuarios2():
    return render_template("index2.html", users3=usuarios3)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8090, debug=True)
