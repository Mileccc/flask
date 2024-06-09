from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def hola_mundo():
    return "Hola mundo!"


@app.route("/hola")
def hola_elegante():
    return """
        <html>
            <body>
                <h1>Hola Elegante</h1>
                <p>Hola Mundo</p>
            </body>
        </html>
    """


@app.route("/primera")
def template_primera():
    return render_template("primera_pagina.html")


@app.route("/segunda")
def template_segunda():
    return render_template("segunda_pagina.html")


@app.route("/variables")
def nombres_variables():
    return render_template("variables.html", nombre="Antonio", curso="Python")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8090)
