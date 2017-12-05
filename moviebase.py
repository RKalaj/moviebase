import os
from flask import Flask, render_template, session, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'our secret key'

# setup SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)


# define database tables
class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    about = db.Column(db.Text)
    movie = db.relationship('Movie', backref='director', cascade="delete")


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    year = db.Column(db.Integer)
    director_id = db.Column(db.Integer, db.ForeignKey('director.id'))


@app.route('/')
def home():
    # return '<h1>hello world!</h1>'
    return render_template('index.html')


@app.route('/about')
def members():
    # return '<h1>hello world!</h1>'
    return render_template('members.html')


@app.route('/directors')
def show_all_directors():
    director = Director.query.all()
    return render_template('director-all.html', director=director)


if __name__ == '__main__':
    app.run(debug=True)
