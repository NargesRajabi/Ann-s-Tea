from flask import Flask, abort, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/about/')
def about():
    return render_template("About.html")

@app.route('/news/')
def news():
    return render_template("news.html")

@app.route('/careers/')
def career():
    return render_template("career.html")

# ...
@app.route('/login/')
def login():
    return render_template("login.html")

@app.route('/register/')
def register():
    return render_template("register.html")

@app.route('/team/')
def team():
    return render_template("team.html")

@app.route('/contact/')
def contact():
    return render_template("contact.html")


@app.route('/users/<int:user_id>/')
def greet_user(user_id):
    users = ['Bob', 'Jane', 'Adam']
    try:
        return '<h2>Hi {}</h2>'.format(users[user_id])
    except IndexError:
        abort(404)

if __name__ == '__main__':
    app.run()
