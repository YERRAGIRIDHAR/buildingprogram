import flask
from flask import *
import json, time

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_page():
    data_set = {"page":"Home","Name": "Giridhar", "Message": "Yes Successfully loaded","Timestamp": time.time()}
    json_dump = json.dumps(data_set)

    return json_dump


@app.route('/user/', methods=['GET'])
def request_page():
    user_query = str(request.args.get('user'))


    data_set = {"page":"Request ", "Name": f"Giridhar", "Message": "Successfully got request for {user_query}","Timestamp": time.time()}
    json_dump = json.dumps(data_set)

    return json_dump

if __name__ == "__main__":
    app.run(debug=True)
