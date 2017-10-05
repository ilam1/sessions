from flask import Flask, render_template, request, redirect, session
import os

app = Flask (__name__)

username = "user"
password = "pwd"
out = ""
is_correct = True
app.secret_key = os.urandom(32)

@app.route("/")
def hello_world():
    print(session)
    print(username in session)
    if username in session:
        return render_template("loggedin.html")

    return render_template("login.html", output = correct())

def correct():
    try:
        user_right = (username == request.args["username"])
        pass_right = (password == request.args["password"])
        if user_right and pass_right:
            session[username] = password
            is_correct = True;
            return "Welcome!"
        elif user_right and not pass_right:
            is_correct = False;
            return "Error: Wrong password"
        else:
            is_correct = False;
            return "Error: Wrong username"
    except:
        pass

@app.route("/loggedin")
def logged_in():
#    print(request.args)
    return render_template("loggedin.html", output = correct(),good = is_correct )

@app.route("/loggedout")
def logged_out():
    session.pop(username) #ending session
    return render_template("login.html", output = correct()) #redirecting to login

if __name__ == '__main__':
    app.debug = True
    app.run()
