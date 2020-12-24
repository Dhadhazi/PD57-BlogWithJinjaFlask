from flask import Flask, render_template
import requests
import datetime

app = Flask(__name__)


def get_data(url):
    res = requests.get(url=url)
    res.raise_for_status()
    return res.json()


def get_gender(name):
    data = get_data(f"https://api.genderize.io?name={name}")
    return data["gender"]


def get_age(name):
    data = get_data(f"https://api.agify.io?name={name}")
    return data["age"]


def get_blog_posts():
    data = get_data("https://api.npoint.io/5abcca6f4e39b4955965")
    return data


@app.route('/')
def home():
    year = datetime.datetime.now().year
    return render_template("index.html", year=year)


@app.route('/guess/<name>')
def guessing(name):
    gender = get_gender(name)
    age = get_age(name)
    return render_template("guess.html", name=name, gender=gender, age=age)


@app.route("/blog")
def blog():
    posts = get_blog_posts()
    return render_template("blog.html", posts=posts)


if __name__ == "__main__":
    app.run(debug=True)