import json
from crypt import methods
from pickle import TRUE
from flask import Flask,render_template,request,redirect,url_for
import pandas as pd
import re
import pymongo
client = pymongo.MongoClient("mongodb+srv://suriya315:12345678s@cluster0.kbh9v.mongodb.net/?retryWrites=true&w=majority")
db = client.store
pc=db.status
app=Flask(__name__)

@app.route("/")

def index():
    return render_template("domperpertis.html")

@app.route("/bill")
def suriya():
    return render_template("bill.html")
@app.route("/summary")
def suri():
    return render_template("summary.html")
@app.route('/test', methods=['POST'])
def test():
    output = request.get_json()
    print(output) # This is the output that was stored in the JSON within the browser
    print(type(output))
    result = json.loads(output)
    name=result["_id"]
    try:
        
        pc.find_one({"_id":name})["_id"]
    except:
        pc.insert_one(result)
        return False
    return True
    print(result) # Printing the new dictionary
    print(type(result))#this shows the json converted as a python dictionary
    return result

if __name__=='__main__':
    app.run(debug=True)
