from flask import Flask, request, render_template, redirect, session
app = Flask(__name__, static_folder="static", static_url_path="/static")
app.secret_key = "45ffh46dfh"

@app.route("/")
def index():
    session["signin"] = False
    return render_template("index.html")

@app.route("/signin", methods=["POST"])
def signin():
    accountPass = "test"
    passwordPass = "test"
    account = request.form["account"]
    password = request.form["password"]
    if (account == accountPass and password == passwordPass):
        session["signin"] = True
        return redirect("/member")
    else:
        return redirect("/error")

@app.route("/member/")
def member():
    if session["signin"] == True:
        return render_template("member.html")
    elif session["signin"] == False:
        return redirect("/")

@app.route("/error/")
def error():
    return render_template("error.html")

@app.route("/signout", methods=["GET"])
def signout():
    session["signin"] = False
    return redirect("/")

if __name__ == "__main__":
    app.run(port=3000)