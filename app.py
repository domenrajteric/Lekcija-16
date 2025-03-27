from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    random_message = "Hello there!"
    current_year = datetime.datetime.now().year
    cities = ["LJ", "MB", "KP"]

    return render_template("index.html", message=random_message, year=current_year)

@app.route("/game")
def game():
    return render_template("game.html")

if __name__ == "__main__":
    app.run()

