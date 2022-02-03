import os, secrets
from flask import Flask, render_template, request

app = Flask(__name__)


@app.get("/")
def hello_world():
    secret = secrets.token_urlsafe(16)
    submit_url = os.environ.get("SERVER_FOO_URL", default="/")
    return render_template("hello.html", secret=secret, submit_url=submit_url)

@app.post("/s")
def submit():
    form = request.form
    print(form)
    return "Thanks"
