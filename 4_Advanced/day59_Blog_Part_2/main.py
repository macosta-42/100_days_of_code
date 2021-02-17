from flask import Flask, render_template
from post import Post
import requests

app = Flask(__name__)

response = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()
post_objects = []
for post in response:
    post_obj = Post(
        post["id"],
        post["title"],
        post["subtitle"],
        post["body"],
        post["author"],
        post["date"],
        post["image_url"]
    )
    post_objects.append(post_obj)


@app.route('/')
def home():
    return render_template('index.html', all_posts=response)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
