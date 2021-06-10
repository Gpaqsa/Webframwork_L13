from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('Home.html')


@app.route('/about')
def about():
    return render_template('about.html')    


@app.route('/staff')
def staff():
    admins = "გიორგი პაქსაშვილის"
    return render_template("staff.html", admins=admins)


@app.route('/user/<name>/<int:age>')
def user(name, age):
    retirement = 65
    pensioner = retirement-age
    return render_template("user.html", name=name, age=age, pensioner=pensioner)


if __name__ == '__main__':
    app.run(debug=True)