from flask import Flask, render_template, request

app = Flask(__name__)


@app.post("/")
def submit():
    return render_template("thanks.html", secret=request.form.get("apd-auth-token", default="error"))
