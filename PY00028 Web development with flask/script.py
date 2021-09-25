from flask import Flask, render_template

Web = Flask(__name__)

@Web.route('/')
def home(): 
    return render_template("home.html")

@Web.route('/about/')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    Web.run(debug= True)