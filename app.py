from flask import Flask, request, render_template, make_response
from flask_restful import Api, Resource, reqparse
from werkzeug import secure_filename
import pandas as pd
import cgitb
import json
import csv
import cgi

BASE = "http://127.0.0.1:5000/"
app = Flask(__name__)
api = Api(app)

@app.route('/', methods=['GET'])
def index():
  header = {'Content-Type': 'text/html'}
  return make_response(render_template('index.html'), 200, header)
     
@app.route('/uploadcsv', methods=['GET', 'POST'])
def upload():
  if request.method=='POST':
    f = request.files['csvfile']
    data = []
    with open(f.filename) as file:
      csvfile = csv.reader(file)
      for row in csvfile:
        data.append(row)
      data = pd.DataFrame(data).to_html(header=False, index=False, classes=["table", "table-bordered", "table-dark text-center"])
    return render_template('index.html', data=data)
  else:
    header = {'Content-Type': 'text/html'}
    return make_response(render_template('index.html'), 200, header)

if __name__ == "__main__":
  app.run(debug=True)