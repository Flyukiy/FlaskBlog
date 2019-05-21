from flask import Flask, render_template, flash, redirect, url_for
from form import RegistirationForm, LoginForm
from flask import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c18caca2c8ecee93eda44c67b08c6ec1'
app.config['SQLAlCHEMY_DATABASE_URI'] = 'sqlite://database.sql'
db = SQLAlchemy(app)

posts = [
        {
            'author': 'Kamoliddin Usmonov',
            'title': 'Blog post 1',
            'data_posted': 'May 19, 2019',
            'content': 'First post content'
        },
        {
            'author': 'Bahodir Usmonov',
            'title': 'Blog post 1',
            'data_posted': 'May 30, 2019',
            'content': 'Seond post content'
        }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title="About")

@app.route("/register", methods=["POST", "GET"])
def register():
    form = RegistirationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Resgister', form=form)

@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
