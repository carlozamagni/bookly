from flask import request, session, redirect, url_for, render_template, Blueprint, flash
from flask.ext.login import login_user, logout_user
from areas.user.models.forms import RegisterForm
from areas.user.models.user import User
import infrastructure
import bson.objectid


__author__ = 'carlozamagni'


user_app = Blueprint('user', __name__, static_folder='static', template_folder='templates')

login_manager = infrastructure.login_manager
admin = infrastructure.admin
db = infrastructure.db

# see: https://github.com/mrjoes/flask-admin/blob/master/examples/auth-mongoengine/auth.py

@login_manager.user_loader
def load_user(user_id):
    return User.objects(id=str(user_id)).first()

@user_app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'GET' and session.has_key('user_home'):
        return redirect(session['user_home'])

    form = RegisterForm()
    if form.validate_on_submit():
        flash('Success')
        user = User()
        form.populate_obj(user)
        user.save()

        return redirect(user.get_user_home())

    return render_template('user/register.html', form=form)

# @user_app.route('/<id>')
@user_app.route('/')
def home():
    user_id = session.get('user_id', None)
    if user_id:
        user = User.objects(id=user_id).first()
        return render_template('user/home.html', user=user)

    return redirect('user/login')

@user_app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']
        try:
            user = User.objects(user_name=username).first()
        except Exception, e:
            user = None

        if user is None or user['password'] != password:
            error = 'Invalid username or password'
        else:
            session['logged_in'] = True
            session['user_id'] = user.get_string_id()
            session['user_home'] = user.get_user_home()

            #home_page = user_model.User.get_role(user['role'])
            login_user(user=user)

            return redirect(user.get_user_home())

    return render_template('user/login.html', error=error)


@user_app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('user_id', None)
    logout_user()
    return redirect(url_for('main_page'))