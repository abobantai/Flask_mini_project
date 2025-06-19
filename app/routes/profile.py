from flask import Blueprint
profile_bp = Blueprint('profile', __name__)


from app import db, models
from flask import render_template, request, redirect, url_for, flash, session


@profile_bp.route('/profile')
def profile():
    user_id = session.get('user_id')
    if not user_id:
        flash('You must be logged in to view your profile.')
        return redirect(url_for('login'))
    

    user = models.User.query.get(user_id)
    if not user:
        flash('User not found.')
        return redirect(url_for('login'))
    

    username = user.username
    userbio = models.Bio.query.filter_by(user_id=user_id).first()
    if userbio:
        bio = userbio.bio
        email = userbio.email
    else:
        bio = None
        email = None
    if userbio.avatar:
        avatar = userbio.avatar
    else:
        avatar = None


    return render_template('profile.html', username=username, bio=bio, email=email, avatar=avatar)