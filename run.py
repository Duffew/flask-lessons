# ensure 2 blank spaces between each of the python functions
# import os to provide a way to interact with the operating system
import os
import json
# import Flask to access the flask modules
from flask import Flask, render_template, request

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
    # initialise an empty array to manage the .json data
    data = []
    # open the .json file as read only and assign the content to json_data
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        # pass the data list into the return statement and call it 'company'
    return render_template("about.html", page_title="About", company=data)


# creta a new route which will dispaly additional company member info when heading is clicked
@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)


# create a function that returns contact.html when called by defining the route to that file
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        print(request.form)
    return render_template("contact.html", page_title="Contact")


# create a function that returns careers.html when called by defining the route to that file
# add a new link now in base.html and create careers.html - use inheritance to copy the base html
@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        # NEVER INCLUDE debug=True IN A PRODUCTION APPLICATION OR A PROJECT SUBMISSION
        # CHANGE TO debug=False BEFORE DEPLOYMENT/SUBMISSION
        debug=True
    )