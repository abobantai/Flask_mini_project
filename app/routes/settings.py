from flask import Blueprint, current_app as app
settings_bp = Blueprint('settings', __name__)

from app import db, models
from flask import render_template, request, redirect, url_for, flash, session
import os
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@settings_bp.route('/settings' , methods=['GET', 'POST'])
def settings():
    if request.method == 'POST':
        user_id = session.get('user_id')
        if not user_id:
            flash('You must be logged in to change settings.')
            return redirect(url_for('auth.login'))
        userbio = models.Bio.query.filter_by(user_id=user_id).first()
        if not userbio:
            flash('Bio not found.')
            return redirect(url_for('settings.settings'))
        
        file = request.files.get('avatar')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            user_id = session['user_id']
            userbio.avatar = filename
            db.session.commit()
        
        bio = request.form.get('bio', '')
        email = request.form.get('email', '')
        
        userbio.bio = bio
        userbio.email = email
        db.session.commit()
        
        flash('Settings updated successfully!')
        return redirect(url_for('settings.settings'))
    else:
        user_id = session.get('user_id')
        if not user_id:
            flash('You must be logged in to access settings.')
            return redirect(url_for('auth.login'))
        user = models.User.query.get(user_id)
        if not user:
            flash('User not found.')
            return redirect(url_for('auth.login'))
        userbio = models.Bio.query.filter_by(user_id=user_id).first()
        if not userbio:
            bio = models.Bio(user_id=user_id, bio='', email='')
            models.db.session.add(bio)
            models.db.session.commit()
        userbio = models.Bio.query.filter_by(user_id=user_id).first()
        if userbio:
            bio = userbio.bio
        elif userbio is None:
            bio = ''
        email = userbio.email if userbio else ''
        if userbio.avatar:
            avatar = userbio.avatar
        else:
            avatar = None
        return render_template('change.html', username=user.username, bio=bio, email=email, avatar=avatar)