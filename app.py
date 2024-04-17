import os
import json
import pandas as pd
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# def getFormat(filename):
#     """
#     Returns the format of a file.
#     """
#     return os.path.splitext(filename)[1][1:]

# def jsontocsv(jsonfile):
#     data = pd.read_json(jsonfile)
#     data.to_csv("./outputs/outputfromjson.csv",index=False)
    
# def csvtojson(csvfile):
#     data = pd.read_csv(csvfile)
#     records = json.loads(data.to_json(orient="records"))
#     with open("./outputs/outputfromcsv.json","w") as f:
#         data = json.dump(records,f)
    
    
# jsontocsv("./dataset/books.json")
# # csvtojson("./dataset/books.csv")