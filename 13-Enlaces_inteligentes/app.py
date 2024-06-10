from flask import Flask, render_template

app = Flask(__name__, static_folder="static")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/singup")
def singup():
    return render_template("singup.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8090, debug=True)
