from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from flask import Flask, make_response, redirect, session, url_for

from app import db
from app.users.models import User
from app.snap.models import Snap

mod = Blueprint('flow', __name__, url_prefix='/flow')

@mod.route('')
def flows():
    if User.query.filter_by(id = session['user_id']).first():
        userSnap = Snap.query.filter_by(user_id = session['user_id'])
        snapList = [dict(date = snap.date, title=snap.title, mini=snap.mini, img=snap.imgName) for snap in userSnap]
        return render_template('flow.html', snapList = snapList)

    else:
        return redirect(url_for('index'))
