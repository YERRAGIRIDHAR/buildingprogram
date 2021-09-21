from enum import unique
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

#from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:Giridhar!123@localhost/giri'
db=SQLAlchemy(app)

class Data(db.Model):
    _tablename_="data"
    id=db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(120), unique=True)
    height_=db.Column(db.Integer)

    def _init_(self, email_, height_):
        self.email_=email_
        self.height_=height_

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    if request.method=='POST':
        email=request.form["email_name"]
        height=request.form["height_name"]
        print(email, height)
        data=Data(email,height)
        db.session.add(data)
        db.session.commit
    return render_template("success.html")


if __name__ == "_main_":
    app.debug = True
    app.run()