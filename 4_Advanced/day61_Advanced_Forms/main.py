from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap


class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='Log In')


app = Flask(__name__)
app.secret_key = "8Sg2GYERAYF$ywhpn8pdD7LL"
Bootstrap(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    my_form = MyForm()
    if my_form.validate_on_submit():
        if my_form.email.data == "admin@email.com" and my_form.password.data == "123456789":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=my_form)


if __name__ == '__main__':
    app.run(debug=True)
