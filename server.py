from flask import Flask, render_template
import requests
from datetime import datetime
app=Flask(__name__)
@app.route("/")
def hello():
    return "Hello"
@app.route("/guess/<username>")
def guess(username):
    response1 = requests.get(url=f"https://api.agify.io?name={username}")
    response2 = requests.get(url=f"https://api.genderize.io?name={username}")
    return render_template('index.html',name=username.title(),gen=response2.json()['gender'],ag=response1.json()['age'],CURRENT_YEAR=datetime.now().year,n="neha")
if __name__=="__main__":

    app.run(debug=True)
