from flask import Flask, request, render_template, redirect, session
from datetime import timedelta
import os

app = Flask(__name__, static_folder="static", static_url_path="/static")
app.config["SECRET_KEY"] = os.urandom(24)
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(days = 1)

@app.route("/")
def index():
    if "user" in session:
        return redirect("/member/")
    else:
        return render_template("index.html")

@app.route("/signin", methods=["POST"])
def signin():
    accountPass = "test"
    passwordPass = "test"
    account = request.form["account"]
    password = request.form["password"]
    if (account == accountPass and password == passwordPass):
        session["user"] = account
        return redirect("/member/")
    else:
        return redirect("/error/")

@app.route("/member/")
def member():
    if "user" in session:
        return render_template("member.html")
    else:
        return redirect("/")

@app.route("/error/")
def error():
    if "user" not in session:
        return render_template("error.html")
    if "user" in session:
        return redirect("/member/")

@app.route("/signout", methods=["GET"])
def signout():
    session.pop("user", None)
    return redirect("/")

if __name__ == "__main__":
    app.run(port=3000)