from flask import Flask, render_template

app = Flask(__name__)

usuarios = [
    ("Iván", """Nacido en Santiago, Iván es un apasionado deportista
que ha representado a su país en múltiples competencias internacionales.
En su tiempo libre, le gusta explorar la naturaleza y practicar diferentes
disciplinas deportivas."""),

    ("Pamela", """Originaria de Buenos Aires, Pamela es una talentosa fotógrafa que
ha capturado paisajes y culturas de más de 40 países. Cuando no está viajando,
le encanta enseñar clases de yoga y meditación."""),

    ("Rodrigo", """Criado en la ciudad de México, Rodrigo es un chef galardonado
que ha trabajado en algunos de los restaurantes más prestigiosos del mundo.
Es conocido por fusionar la cocina tradicional mexicana con técnicas modernas."""),

    ("Rocío", """Originaria de Jalisco, Rocío es la orgullosa dueña de una finca donde
cultiva agave, ingrediente principal para la producción de tequila.
Ama la vida en el campo y está comprometida con prácticas agrícolas sostenibles.""")
]


@app.route("/")
def inicio():
    return render_template("index.html", users=usuarios)


@app.route("/<username>")
def perfil_usuario(username):
    user_found = None
    for user in usuarios:
        if user[0] == username:
            user_found = user
            break
    if user_found:
        return render_template("perfil.html", user=user_found)
    else:
        return render_template("error.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8090, debug=True)
