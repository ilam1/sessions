from flask import Flask, render_template, request, redirect

app = Flask (__name__)

username = "user"
password = "pwd"
out = ""
@app.route("/")
def hello_world():
    #print(request.args)
    #print(request.args["username"] == username and request.args["password"] == password)
    return render_template("login.html", output = out)

def correct():
    user_right = (username == request.args["username"])
    pass_right = (password == request.args["password"])
    if user_right and pass_right:
        return "Welcome!"
    elif user_right and not pass_right:
        return "Error: Wrong password"
    else:
        return "Error: Wrong username"

@app.route("/loggedin")
def logged_in():
    print(request.args)
    '''
    if correct() == 0:
        out = "Welcome!"
    elif correct() == 1:
        out = "Error: Wrong password"
        return redirect("/")
    else:
        out = "Error: Wrong username"
        return redirect("/")
    '''

    return render_template("loggedin.html", output = correct())

if __name__ == '__main__':
    app.debug = True
    app.run()