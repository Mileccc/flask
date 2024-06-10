from flask import Flask, render_template

app = Flask(__name__)

items = [
    {"nombre": "Mouse", "cantidad": 10},
    {"nombre": "Teclado", "cantidad": 5},
    {"nombre": "Monitor", "cantidad": 1},
]


@app.route("/")
def inicio():
    return render_template("main.html", title="Mi sitio Web")


@app.route("/tienda")
def tienda():
    return render_template(
        "tienda.html",
        nombre="PComponentes",
        direccion="Calle Falsa 123",
        empleados=["Pamela", "Antonio", "Ana"],
        items=items
    )


@app.route("/items")
def lista_item():
    return render_template("items.html", items=items)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8090, debug=True)
