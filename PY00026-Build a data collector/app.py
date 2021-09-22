from enum import unique
from typing import Text
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from send_email import send_email
from sqlalchemy.sql import func


app = Flask(__name__)

'''Connecting to database'''

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:Giridhar!123@localhost/giri'
db=SQLAlchemy(app)

class Data(db.Model):
    _tablename_="data"

    '''for creating columns'''

    id=db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(120), unique=True)
    height_=db.Column(db.Integer)

    def __init__(self, email, height_):
        self.email= email
        self.height_= height_

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    if request.method=='POST':
        email=request.form["email_name"]
        height=request.form["height_name"]
        if db.session.query(Data).filter(Data.email == email).count() == 0:
            data=Data(email,height)
            db.session.add(data)
            db.session.commit()
            average_height=db.session.query(func.avg(Data.height_)).scalar()
            average_height=round(average_height,1)
            count = db.session.query(Data.height_).count()
            send_email(email, height, average_height, count)
            return render_template("success.html")
    return render_template("index.html" , text = "Email already exist")


if __name__ == "__main__":
    app.debug = True
    app.run()