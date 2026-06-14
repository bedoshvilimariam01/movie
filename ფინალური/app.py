from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from models import db, User, Movie, Review
from forms import RegisterForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/")
def index():
    movies = Movie.query.all()
    return render_template("index.html", movies=movies)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data
        )

        db.session.add(user)
        db.session.commit()

        flash("Registration successful!")
        return redirect(url_for("login"))

    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(
            username=form.username.data
        ).first()

        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for("index"))

    return render_template("login.html", form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/movie/<int:id>")
def movie_details(id):
    movie = Movie.query.get_or_404(id)
    return render_template("movie_details.html", movie=movie)

@app.route("/about")
def about():
        return render_template("about.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

        if Movie.query.count() == 0:
            movie1 = Movie(
                title="Oldboy",
                year=2003,
                description="A man is imprisoned for years and seeks revenge.",
                image="oldboy.jpg"
            )

            movie2 = Movie(
                title="The Gangster, the Cop, the Devil",
                year=2019,
                description="A gangster and detective hunt a serial killer.",
                image="gangster.jpg"
            )

            movie3 = Movie(
                title="The Call",
                year=2020,
                description="Two women communicate through time.",
                image="thecall.jpg"
            )

            db.session.add_all([movie1, movie2, movie3])
            db.session.commit()

    app.run(debug=True)
    from forms import RegisterForm, LoginForm, MovieForm


