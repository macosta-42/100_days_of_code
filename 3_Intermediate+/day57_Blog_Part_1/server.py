from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)

current_year = datetime.today().year
genderize = "https://api.genderize.io?name="
agify = "https://api.agify.io?name="


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    return render_template('start.html', num=random_number, year=current_year)


@app.route('/guess/<name>')
def guess(name):
    response = requests.get(genderize + name)
    gender = response.json()['gender']
    response = requests.get(agify + name)
    age = response.json()['age']
    return render_template('age.html', name=name, gender=gender, age=age)


@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/5abcca6f4e39b4955965"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)