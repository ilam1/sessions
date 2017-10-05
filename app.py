from flask import Flask, render_template, request, redirect, session
import os

app = Flask (__name__)

global the__username = "user"
global the_password = "pwd"
out = ""
is_correct = True
app.secret_key = os.urandom(32)

@app.route("/")
def hello_world():
    if "username" in session.keys():
       return render_template("loggedin.html", name = session["username"])
    return render_template("login.html", output = "")

   ''' print(session)
    print(username in session)
    if username in session:
        return render_template("loggedin.html")

    return render_template("login.html", output = correct())
'''
   
''' 
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

'''
@app.route("/loggedin")
def logged_in():
#    print(request.args)
   input_name = request.args["username"]
   input_pass = request.args["password"]
   #CHECKING
   if input_name == the_username:
      if input_pass == the_password:
         session["username"] = input_name #new sess
         return render_template("loggedin.html", name = input_name)
      else:
         return return_template("login.html", output = "Error: Wrong password")
   else:
      return render_template("login.html", output =  "Error: Wrong username")

@app.route("/logout")
def logged_out():
    session.pop("username") #ending sess
    return render_template("login.html", output = "") #redirecting to login

if __name__ == '__main__':
    app.debug = True
    app.run()
