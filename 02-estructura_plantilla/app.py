from flask import Flask, render_template

app = Flask(__name__)


class Pelicula():
    def __init__(self, nombre, anio, protagonista):
        self.nombre = nombre
        self.anio = anio
        self.protagonista = protagonista


@app.route("/estructura")
def estructura_datos():
    peliculas = [
        "El lobo de Wall Street",
        "El gran leon",
        "Titanic"
    ]

    lobo = {
        "Nombre": "El lobo de Wall Street",
        "Anio": 2013,
        "Protagonista": "Leonardo DiCaprio"
    }

    volver = Pelicula("Volver al futuro", 1985, "Michael J. Fox")

    return render_template("estructuras.html", movies=peliculas, destacada=lobo, favorita=volver)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8090)
