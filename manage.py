from flask_script import Manager
from moviebase import app, db, Director, Movie

manager = Manager(app)


@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    nolan = Director(name='Christopher Nolan', about='Christopher Edward Nolan is an English film director, screenwriter, and producer who holds both British and American citizenship. He is one of the highest-grossing directors in history, and among the most acclaimed filmmakers of the 21st century.')
    jackson = Director(name='Peter Jackson', about='Sir Peter Robert Jackson is a New Zealand film director, screenwriter and film producer. He is best known as the director, writer, and producer of The Lord of the Rings trilogy (2001-03) and The Hobbit trilogy (2012-14), both of which are adapted from the novels of the same name by J. R. R. Tolkien.')
    tarantino = Director(name='Quentin Tarantino', about='Quentin Jerome Tarantino is an American film director, writer, and actor. His filmsare characterized by nonlinear storylines, satirical subject matter, an aestheticization of violence, extended scenes of dialogue, ensemble casts consisting of established and lesser-known performers, references to popular culture, soundtracksprimarily containing songs and score pieces from the 1960s to the 1980s, and features of neo-noir film. He is widely considered one of the greatest filmmakers of his generation.')
    interstellar = Movie(name='Interstellar', year=2014, director=nolan)
    lotr3 = Movie(name='The Lord of the Rings: The Return of the King', year=2003, director=jackson)
    inglourious = Movie(name='Inglourious Basterds', year=2009, director=tarantino)
    db.session.add(nolan)
    db.session.add(jackson)
    db.session.add(tarantino)
    db.session.add(interstellar)
    db.session.add(lotr3)
    db.session.add(inglourious)
    db.session.commit()


if __name__=='__main__':
    manager.run()
