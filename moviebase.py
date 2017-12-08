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
    about = db.Column(db.Text)
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
    return render_template('directors-all.html', director=director)


@app.route('/directors/add', methods=['GET', 'POST'])
def add_directors():
    if request.method == 'GET':
        return render_template('directors-add.html')
    if request.method == 'POST':
        # get data from the form
        name = request.form['name']
        about = request.form['about']

        # insert the data into the database
        director = Director(name=name, about=about)
        db.session.add(director)
        db.session.commit()
        return redirect(url_for('show_all_directors'))


@app.route('/directors/edit/<int:id>', methods=['GET', 'POST'])
def edit_directors(id):
    director = Director.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('directors-edit.html', director=director)
    if request.method == 'POST':
        # update data based on the form data
        director.name = request.form['name']
        director.about = request.form['about']
        # update the database
        db.session.commit()
        return redirect(url_for('show_all_directors'))


@app.route('/directors/delete/<int:id>', methods=['GET', 'POST'])
def delete_director(id):
    director = Director.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('directors-delete.html', director=director)
    if request.method == 'POST':
        # delete the artist by id
        # all related songs are deleted as well
        db.session.delete(director)
        db.session.commit()
        return redirect(url_for('show_all_directors'))


@app.route('/movies')
def show_all_movies():
    movie = Movie.query.all()
    return render_template('movies-all.html', movie=movie)


@app.route('/movies/add', methods=['GET', 'POST'])
def add_movies():
    if request.method == 'GET':
        director = Director.query.all()
        return render_template('movies-add.html', director=director)
    if request.method == 'POST':
        # get data from the form
        name = request.form['name']
        year = request.form['year']
        about = request.form['about']
        director_name = request.form['director']
        director = Director.query.filter_by(name=director_name).first()
        movie = Movie(name=name, year=year, about=about, director=director)

        # insert the data into the database
        db.session.add(movie)
        db.session.commit()
        return redirect(url_for('show_all_movies'))


@app.route('/movies/edit/<int:id>', methods=['GET', 'POST'])
def edit_movies(id):
    movie = Movie.query.filter_by(id=id).first()
    director = Director.query.all()
    if request.method == 'GET':
        return render_template('movies-edit.html', movie=movie, director=director)
    if request.method == 'POST':
        # update data based on the form data
        movie.name = request.form['name']
        movie.year = request.form['year']
        movie.about = request.form['about']
        director_name = request.form['director']
        director = Director.query.filter_by(name=director_name).first()
        movie.director = director
        # update the database
        db.session.commit()
        return redirect(url_for('show_all_movies'))


@app.route('/movies/delete/<int:id>', methods=['GET', 'POST'])
def delete_movies(id):
    movie = Movie.query.filter_by(id=id).first()
    director = Director.query.all()
    if request.method == 'GET':
        return render_template('movies-delete.html', movie=movie, director=director)
    if request.method == 'POST':
        # use the id to delete the song
        # song.query.filter_by(id=id).delete()
        db.session.delete(movie)
        db.session.commit()
        return redirect(url_for('show_all_movies'))


if __name__ == '__main__':
    app.run(debug=True)
