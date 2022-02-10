from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_app import app

from flask_bcrypt import Bcrypt
bcrypt=Bcrypt(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/register", methods=['POST'])
def register():
    if not User.validate_user(request.form):
        return redirect('/')

    data={}
    for form_field, form_field_data in request.form.items():
        data[form_field]=form_field_data
    data['password']=bcrypt.generate_password_hash(request.form['password'])

    user_id=User.save(data)
    session['user_id']=user_id
    return redirect('/quotes')

@app.route("/login", methods=['POST'])
def login():
    user=User.authenticate_user(request.form['email'], request.form['password'])
    if user:
        session['user_id']=user.id
        return redirect('/quotes')
    else:
        return redirect('/')

