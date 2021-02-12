from flask import Flask
import random

app = Flask(__name__)

number = random.randint(0, 9)


@app.route('/')
def home():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/ne3xrYlWtQFtC/giphy.gif" alt="a number gif">'


@app.route('/<int:guess>')
def result(guess):
    if guess < number:
        color = "%06x" % random.randint(0, 0xFFFFFF)
        return f'<h1 style="color:{color};">Too low, try again!</h1>' \
               f'<img src="https://media.giphy.com/media/IevhwxTcTgNlaaim73/giphy.gif" alt="too low gif">'
    elif guess > number:
        color = "%06x" % random.randint(0, 0xFFFFFF)
        return f'<h1 style="color:{color};">Too high, try again!</h1>' \
               f'<img src="https://media.giphy.com/media/CBnXOLstPIoTmqLryW/giphy.gif" alt="too high gif">'
    else:
        color = "%06x" % random.randint(0, 0xFFFFFF)
        return f'<h1 style="color:{color};">You found me!</h1>' \
               f'<img src="https://media.giphy.com/media/naiba7cRbSjgrzJ9wa/giphy.gif" alt="found me gif">'


if __name__ == "__main__":
    app.run(debug=True)
