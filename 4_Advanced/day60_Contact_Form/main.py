from flask import Flask, render_template, request
from post import Post
import requests
import smtplib

# Change the receiver email here
EMAIL_TO = ""

# Change your email and password here
EMAIL_FROM = ""
PASSWORD = ""

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


@app.route('/contact', methods=['GET', 'POST'])
def receive_data():
    if request.method == 'POST':
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL_FROM, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL_FROM,
                to_addrs=EMAIL_TO,
                msg=f"Subject: New Contact\n\n"
                    f"Name: {request.form['username']}\n"
                    f"Email: {request.form['email']}\n"
                    f"Phone: {request.form['phone']}\n"
                    f"Message: {request.form['message']}".encode('ascii', errors='ignore')
            )
        return render_template('contact.html', msg_sent=True)
    else:
        return render_template('contact.html', msg_sent=False)


@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
