from flask import Flask, request, render_template
from flask.helpers import send_file
#from flask.templating import render_template
from geopy.geocoders import Nominatim
import pandas
import datetime

app = Flask('__name__')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success_table', methods = ["POST"])
def success_table():
    global filename
    if request.method == ["POST"]:
        file = request.files("file")
        try:
            df = pandas.read_csv(file)
            gc = Nominatim()
            '''To extract longitude and latitude from address'''
            df['coordinates'] = df['Address'].apply(gc.geocode)
            df['Latitude'] = df['coordinates'].apply(lambda x: x.latitude if x != None else None)
            df['Longitude'] = df['coordinates'].apply(lambda x: x.longitude if x != None else None)
            df = df.drop("coordinates",1)
            filename = datetime.now().strftime("uploads/%Y-%m-d%-H%-M%-S%-f%" + ".csv") #To generate file name with date
            df.to_csv(filename, index = None)
            return render_template("index.html", text= df.to_html(), btn="download.html")
        except Exception as e:
            return render_template("index.html", text=str(e))

@app.route('/download-file/')

def download():
    return send_file(filename, attachment_filename='yourfile.csv',as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)