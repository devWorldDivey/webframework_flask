from flask import Flask,render_template,url_for

app = Flask(__name__)
app.config["SECRET_KEY"]="qwerty12345"

from routes import *

if __name__ == "__main__":
    app.run(debug=True)