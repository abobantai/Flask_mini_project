from flask import Blueprint
auth_bp = Blueprint('auth', __name__)

from app import db, models
from flask import render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash


@auth_bp.route('/')
def index():
    return render_template('index.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        user = models.User.query.filter_by(username=username).first()
        users = models.User.query.all()
        print(f"Registering user: {users}")
        if user:
            return render_template('register.html', error='Username already exists')
        if password != confirm_password:
            return render_template('register.html', error='Passwords do not match')
        if len(password) < 6:
            return render_template('register.html', error='Password must be at least 6 characters long')
        if not username or not password:
            return render_template('register.html', error='Username and password are required')
        
        password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
        print(f"Username: {username}, Password: {password}, Confirm Password: {confirm_password}")
        
        new_user = models.User(username=username, password=password)
        models.db.session.add(new_user)
        models.db.session.commit()
        flash('Registration successful! Please log in.')
        return redirect(url_for('auth.login'))
    if request.method == 'GET':
        return render_template('register.html')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = models.User.query.filter_by(username=username).first()
        if user:
            if not check_password_hash(user.password, password):
                flash('Invalid username or password')
                return render_template('login.html')
            else:
                session['user_id'] = user.id
                flash('Login successful!')
                return redirect(url_for('profile.profile', userid=user.id))
        else:
            flash('Invalid username or password')
            return render_template('login.html')
    return render_template('login.html')



@auth_bp.route('/logout')
def logout():
    return render_template('index.html')
