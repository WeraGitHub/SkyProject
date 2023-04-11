from flask import render_template
from application import app


@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    title_name = "Home"
    var = ""
    return render_template('home.html', title=title_name)


@app.route('/welcome/<name>')
def welcome(name):
    return render_template('welcome.html', name=name, group="Everyone")


@app.route('/')
def index():
    title_name = "Index"
    return render_template('home.html', title=title_name)


@app.route('/practice')
def practice():
    return render_template('practice.html', title="practice")


@app.route('/about')
def about():
    return render_template('about.html', title="About")


@app.route('/favourite')
def favourite():
    return render_template('favourite.html', title="Favourite", list_of_things=['chocolate', 'dogs', 'sunsets'])
