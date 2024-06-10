from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = '123456'

users = {}
print(users)


@app.route("/")
def index():
    user = session.get('user')
    if user:
        return f"Bienvenido {user}"
    return "Bienvenido a la aplicación de registro de usuarios."


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        session['user'] = username
        users[username] = password
        print(users)
        return redirect(url_for("index"))
    return render_template("register.html")


@app.route("/logout")
def logout():
    session.pop('user', None)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8090, debug=True)
