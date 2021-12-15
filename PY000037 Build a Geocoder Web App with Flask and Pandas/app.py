from flask import Flask, request, render_template
from flask.helpers import send_file
from geopy import geocoders
from geopy.geocoders import Nominatim
import  datetime
import pandas

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/success_table', methods = ['POST'])
def success_table():
    global filename
    if request.method == "POST":
        file = request.files["file"]
        df = pandas.read_csv(file)
        try:
            gc = Nominatim(user_agent="PY000037 Build a Geocoder Web App with Flask and Pandas")
            df["coordinates"] = df["Address"].apply(gc.geocode)
            df["Latitude"] = df["coordinates"].apply(lambda x: x.latitude if x != None else None)
            df["Longitude"] = df["coordinates"].apply(lambda x: x.longitude if x != None else None)
            df=df.drop("coordinates", 1)
            filename=datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f"+".csv") #To generate file name with date
            df.to_csv(filename, index = None)
            return render_template("index.html", text=df.to_html(), btn="download.html")
        except:
            return render_template("index.html", text = "Please upload csv file")

@app.route('/download-file/')

def download():
    return send_file(filename, attachment_filename=filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)