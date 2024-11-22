# import os to provide a way to interact with the operating system
import os
# import Flask to access the flask modules
from flask import Flask

# create an instance of the flask class called 'app'
app = Flask(__name__)

# when we try to browse to the root directory "/" the index function will trigger
# after typing all the following, Flask should run successfully
@app.route("/")
def index():
    return "Hello World"

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        # NEVER INCLUDE debug=True IN A PRODUCTION APPLICATION OR A PROJECT SUBMISSION
        # CHANGE TO debug=False BEFORE DEPLOYMENT/SUBMISSION
        debug=True
    )