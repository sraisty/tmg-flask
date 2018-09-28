"""
Main Server file


"""

from flask import Flask, request, render_template, session, redirect
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

def connect_to_db(app):
    """ Connect to database """
    app.config['SQLALCHEMY_DATABASE_URI'] = '/postgresql:///tmg_database'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)

@app.route('/')
def show_index():
    return render_template("index.html")



##### MAIN  ######
app = Flask(__name__)
app.secret_key = "DFLDSJFLEWR@#TGFV")  # TODO I random generated this by typing
connect_to_db(app)

if __name__ == "__main__":
    app.debug = True
    DebugToolbarExtension(app)
    app.run(debug=True)