import os
from flask import Flask
from flask import render_template
from flask import request,jsonify

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

project_dir = os.path.dirname(os.path.abspath(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///{}".format(os.path.join(project_dir, "bookdatabase.db"))

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

@app.route("/", methods=["GET", "POST"])
def home():
    if request.form:
        user=User()
        user.username=request.form.get('username')
        user.email=request.form.get('email')
        db.session.add(user)
        db.session.commit()
    data=User.query.all()
    return render_template("home.html",data=data)




app.run()
