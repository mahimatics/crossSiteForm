import os
from flask import Flask, render_template, request

app = Flask(__name__)


@app.get("/")
def hello_world():
    secret = "?w5J;#2w6phZ^MJt'k:e{ $uUrnR%%:4OQh6eY4Sduuor|01{2UmNMr;yhKKQMk$"
    submit_url = os.environ.get("SERVER_FOO_URL", default="/")
    return render_template("hello.html", secret=secret, submit_url=submit_url)

@app.post("/s")
def submit():
    form = request.form
    print(form)
    return "Thanks"
