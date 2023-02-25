

from flask import Flask, render_template, request
import time

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def countdown():
    minutes = int(request.form["minutes"])
    seconds = int(request.form["seconds"])
    countdown_time = minutes * 60 + seconds

    while countdown_time:
        mins, secs = divmod(countdown_time, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat)
        time.sleep(1)
        countdown_time -= 1

    return "Countdown finished!"

if __name__ == "__main__":
    app.run(debug=True)
