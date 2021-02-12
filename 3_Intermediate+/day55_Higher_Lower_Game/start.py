# from flask import Flask
#
# app = Flask(__name__)
#
#
# def make_bold(function):
#     def wrapper():
#         return f"<b>{function()}</b>"
#     return wrapper
#
#
# def make_emphasis(function):
#     def wrapper():
#         return f"<em>{function()}</em>"
#     return wrapper
#
#
# def make_underlined(function):
#     def wrapper():
#         return f"<u>{function()}</u>"
#     return wrapper
#
#
# @app.route('/')
# def hello_world():
#     return 'Hello, World'
#
#
# @app.route("/bye")
# @make_bold
# @make_emphasis
# @make_underlined
# def say_bye():
#     return "Bye"
#
#
# @app.route("/username/<name>/<int:number>")
# def greet(name, number):
#     return f"Hello {name}, your are {number} years old!"
#
#
# class User:
#     def __init__(self, name):
#         self.name = name
#         self.is_logged_in = False
#
#
# def is_authenticated_decorator(function):
#     def wrapper(*args, **kwargs):
#         if args[0].is_logged_in:
#             function(args[0])
#     return wrapper
#
#
# @is_authenticated_decorator
# def create_blog_post(user):
#     print(f"This is {user.name}'s new blog post.")
#
#
# new_user = User("angela")
# new_user.is_logged_in = True
# create_blog_post(new_user)
#
#
# def logging_decorator(function):
#     def wrapper(*args, **kwargs):
#         print(f"You called {function.__name__}{args}\n" \
#               f"It returned {function(args[0], args[1], args[2])}")
#     return wrapper
#
#
# @logging_decorator
# def a_function(a, b, c):
#     return a * b * c
# 
#
# a_function(1, 2, 3)
#
#
# if __name__ == "__main__":
#     app.run(debug=True)
