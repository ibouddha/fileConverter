import os
import json
import pandas as pd
from flask import Flask
from flask import render_template, request, redirect, url_for
from flask import make_response

# @app.errorhandler(404)
# def not_found(error):
#     resp = make_response(render_template('error.html'), 404)
#     resp.headers['X-Something'] = 'A value'
#     return resp

app = Flask(__name__)

def jsontocsv(jsonfile):
    data = pd.read_json(jsonfile)
    data.to_csv("./outputs/outputfromjson.csv",index=False)
    
def csvtojson(csvfile):
    data = pd.read_csv(csvfile)
    records = json.loads(data.to_json(orient="records"))
    with open("./outputs/outputfromcsv.json","w") as f:
        data = json.dump(records,f)
        
def readcsv(filename):
    data = pd.read_csv(filename)
    data_var = data.to_html()
    return data_var

def readjson(filename):
    data = pd.read_json(filename)
    data_var = data.to_json()
    return data_var

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/upload",methods=['POST'])
def convert():
    if request.method == 'POST':
        file = request.files['uploaded']
        if file.filename == '':
            print("no file selected")
            return redirect(request.url)
        else:
            formatfile = getFormat()
            match(formatfile):
                case "json":
                    data = readjson(file)
                    print(data)
                    
                case "csv":
                    data = readcsv(file)
                    print(data)
                    
                case _:
                    print("file format not supported")
                
                
            print(data)
            return render_template("index.html", value = data)
    
def getFormat():
    """
    Returns the format of a file.
    """
    
    file = request.files['uploaded']
    return os.path.splitext(file.filename)[1][1:]
    
if __name__ == "__main__":
    app.run(debug=True)



    
    
# jsontocsv("./dataset/books.json")
# # csvtojson("./dataset/books.csv")