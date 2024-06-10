from flask import Flask, render_template

app = Flask(__name__)

cards = [
    {
        "title": "Biografía",
        "content": "<p>Esta es una breve biografía del usuario...</p>"
    },
    {
        "title": "Proyectos",
        "content": "<ul><li>Proyecto 1</li><li>Proyecto 2</li></ul>"
    },
    {
        "title": "Contacto",
        "content": "<p>Email: usuario@example.com</p><p>Teléfono: 123-456-7890</p>"
    }
]


@app.route("/")
def index():
    return render_template("index.html", cards=cards)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8090, debug=True)
