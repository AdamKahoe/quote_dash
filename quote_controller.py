
from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.quote import Quote


@app.route("/quotes")
def quotes():
    if 'user_id' in session:
        user=User.get_by_id(session['user_id'])

        return render_template('quote_dashboard.html', quotes=Quote.get_all_with_users())
    return redirect('/')


