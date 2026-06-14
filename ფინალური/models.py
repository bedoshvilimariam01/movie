from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )

    email = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(100),
        nullable=False
    )


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(100))
    year = db.Column(db.Integer)
    description = db.Column(db.Text)
    image = db.Column(db.String(100))


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    text = db.Column(db.Text)

    movie_id = db.Column(
        db.Integer,
        db.ForeignKey('movie.id')
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id')
    )