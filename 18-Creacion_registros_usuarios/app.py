from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = {}
print(users)


@app.route("/")
def index():
    return "Bienvenido a la aplicación de registro de usuarios."


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        users[username] = password
        print(users)
        return redirect(url_for("index"))
    return render_template("register.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8090, debug=True)
