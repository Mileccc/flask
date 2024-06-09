from flask import Flask, render_template

app = Flask(__name__)

variable = ["Ivan", "Pamela", "Antonio"]


@app.route("/")
def index():
    return render_template("index.html", var=variable)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8090, debug=True)
