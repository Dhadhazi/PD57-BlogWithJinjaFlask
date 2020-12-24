from flask import Flask, render_template
import requests

app = Flask(__name__)


def get_data(url):
    res = requests.get(url=url)
    res.raise_for_status()
    return res.json()


def get_blog_posts():
    data = get_data("https://api.npoint.io/5abcca6f4e39b4955965")
    return data

posts = get_blog_posts()

@app.route('/')
def home():
    return render_template("index.html", posts=posts)


@app.route('/post/<int:id>')
def post_page(id):
    for post in posts:
        if post["id"] == id:
            requested_post = post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
