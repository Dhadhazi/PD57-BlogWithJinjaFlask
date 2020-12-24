from flask import Flask, render_template
import requests
import datetime

app = Flask(__name__)


def get_gender(name):
    res = requests.get(url=f"https://api.genderize.io?name={name}")
    res.raise_for_status()
    data = res.json()
    return data["gender"]


def get_age(name):
    res = requests.get(url=f"https://api.agify.io?name={name}")
    res.raise_for_status()
    data = res.json()
    return data["age"]


@app.route('/')
def home():
    year = datetime.datetime.now().year
    return render_template("index.html", name="Dani", year=year)


@app.route('/guess/<name>')
def guessing(name):
    gender = get_gender(name)
    age = get_age(name)
    return render_template("guess.html", name=name, gender=gender, age=age)


if __name__ == "__main__":
    app.run(debug=True)