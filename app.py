from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        number1 = random.randint(0, 20)
        number2 = random.randint(0, 20)

        return render_template("index.html", number1=number1, number2=number2, streak=0)
    else:
        number1 = int(request.form.get("number1"))
        number2 = int(request.form.get("number2"))
        result = number1 * number2

        streak = int(request.form.get("streak"))

        answer = request.form.get("answer")

        if answer and answer.isdigit() and int(answer) == result:
            message = f"Correct answer! :) {number1} x {number2} = {result}"
            streak += 1
        else:
            message = f"Wrong answer! :( {number1} x {number2} = {result}"
            streak = 0

        number1 = random.randint(0, 25)
        number2 = random.randint(0, 25)

        return render_template("index.html", message=message, number1=number1, number2=number2, streak=streak)

if __name__ == "__main__":
    app.run()

