from flask import Flask, render_template, request, redirect, session
import os

app = Flask (__name__)

username = "user"
password = "pwd"
out = ""
app.secret_key = os.urandom(32)

@app.route("/")
def hello_world():
    return render_template("login.html")

def correct():
    user_right = (username == request.args["username"])
    pass_right = (password == request.args["password"])
    if user_right and pass_right:
        session[username] = password
        return "Welcome!"
    elif user_right and not pass_right:
        return "Error: Wrong password"
    else:
        return "Error: Wrong username"

@app.route("/loggedin")
def logged_in():
#    print(request.args)
    return render_template("loggedin.html", output = correct())

if __name__ == '__main__':
    app.debug = True
    app.run()