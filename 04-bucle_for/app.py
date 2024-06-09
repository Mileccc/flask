from flask import Flask, render_template

app = Flask(__name__)


@app.route("/for-loop")
def loop_for():
    equipos = [
        "REAL MADRID",
        "BARCELONA",
        "ATLETICO DE MADRID",
        "SEVILLA",
        "VILLARREAL",
        "REAL SOCIEDAD",
        "MACHESTER CITY",
        "BILBAO",
        "BAYERN MUNICH",
        "LIVERPOOL"
    ]

    equipos_champ = {
        "REAL MADRID": 14,
        "BARCELONA": 12,
        "ATLETICO DE MADRID": 11,
        "SEVILLA": 10,
        "VILLARREAL": 9,
        "REAL SOCIEDAD": 8,
        "MACHESTER CITY": 7,
        "BILBAO": 6,
        "BAYERN MUNICH": 5,
        "LIVERPOOL": 4
    }

    return render_template("for_loop.html", teams=equipos, teams_dict=equipos_champ)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8090, debug=True)
