from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash
from flask import Flask, make_response, redirect, session, url_for

from app import db
from app.users.models import User
from app.snap.models import Snap

mod = Blueprint('flow', __name__, url_prefix='/flow')

@mod.route('')
def flows():
	if User.query.filter_by(userEmail = session['user']).first():      
		#user =  User.query.filter_by(userEmail = session['user']).first()
		#userSnap = Snap.query.filter_by(user_id = user.getId()).first()
		#snapList = [dict(date = snap.date, title=snap.title, mini=snap.mini, img=snap.imgName) for snap in userSnap]


		userSnap = Snap.query.all()
		snapList = [dict(date = snap.date, title=snap.title, mini=snap.mini, img=snap.imgName) for snap in userSnap]

		return render_template('flow.html', snapList = snapList)
    
	return redirect(url_for('index'))
