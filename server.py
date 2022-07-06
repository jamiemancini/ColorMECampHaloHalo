from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

# db = SQLALchemy()

def connect_to_db(app):
    """Connect to the database"""

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///database-name"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

app = Flask(__name__)

@app.route('/')
def home():
    """index page"""
    return render_template('homepage.html')

@app.route('/login')
def login():
    """login the user"""
    return render_template('login.html')

@app.route('/register')
def register():
    """register the user"""
    return render_template('register.html')



if __name__ == '__main__':
    app.run(debug=True)
