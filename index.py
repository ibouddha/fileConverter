import os
import json
import pandas as pd

def getFormat(filename):
    """
    Returns the format of a file.
    """
    return os.path.splitext(filename)[1][1:]

def jsontocsv(jsonfile):
    data = pd.read_json(jsonfile)
    data.to_csv("./outputs/output.csv",index=False)
    
def csvtojson(csvfile):
    data = pd.read_csv(csvfile)
    records = json.loads(data.to_json(orient="records"))
    with open("./outputs/output.json","w") as f:
        data = json.dump(records,f)
    
    
jsontocsv("./dataset/books.json")
# csvtojson("./dataset/books.csv")