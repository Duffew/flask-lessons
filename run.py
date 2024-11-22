# ensure 2 blank spaces between each of the python functions
# import os to provide a way to interact with the operating system
import os
# import Flask to access the flask modules
from flask import Flask, render_template

# create an instance of the flask class called 'app'
app = Flask(__name__)


# when we try to browse to the root directory "/" the index function will trigger
# after typing all the following, Flask should run successfully
@app.route("/")
def index():
    return render_template("index.html")


# create a function that returns about.html when called by defining the route to that file
@app.route("/about")
def about():
    return render_template("about.html")


# create a function that returns contact.html when called by defining the route to that file
@app.route("/contact")
def contact():
    return render_template("contact.html")


# create a function that returns careers.html when called by defining the route to that file
# add a new link now in base.html and create careers.html - use inheritance to copy the base html
@app.route("/careers")
def careers():
    return render_template("careers.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        # NEVER INCLUDE debug=True IN A PRODUCTION APPLICATION OR A PROJECT SUBMISSION
        # CHANGE TO debug=False BEFORE DEPLOYMENT/SUBMISSION
        debug=True
    )