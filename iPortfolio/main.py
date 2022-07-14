from flask import Flask, render_template, redirect, url_for, flash, abort
from markupsafe import escape
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask_gravatar import Gravatar
from functools import wraps
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/project1')
def project1():
    return render_template("project1.html")

@app.route('/project2')
def project2():
    return render_template("project2.html")

@app.route('/project3')
def project3():
    return render_template("project3.html")

@app.route('/project4')
def project4():
    return render_template("project4.html")

@app.route('/project5')
def project5():
    return render_template("project5.html")

if __name__ == "__main__":
    app.run()
