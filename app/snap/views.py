import os
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
from app import db, app
from app.snap.models import Snap
from app.users.models import User

mod = Blueprint('snap', __name__, url_prefix='/snap')
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


#SnapUpload
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@mod.route('/json')
def json():

        #    userSnap = Snap.query.filter_by(user_id = session['user_id'])
        #snapList = [dict(date = snap.date, title=snap.title, mini=snap.mini, img=snap.imgName) for snap in userSnap]
        #return render_template('flow.html', snapList = snapList)

    userSnap = Snap.query.all()
    snapList = [dict(title=snap.title, mini=snap.mini, image="http://0.0.0.0:7000/static/uploads/"+snap.imgName) for snap in userSnap]

    return jsonify(result=snapList)

@mod.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['snap']
        userId = session['user_id']

        filename = secure_filename(file.filename)
        #craet instance
        snap = Snap(request.form['title'], request.form['mini'], filename, userId)
        db.session.add(snap)
        db.session.commit()
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    return redirect(url_for('flow.flows'))

@mod.route('/uploadM', methods=['GET', 'POST'])
def upload2():
    file = request.files['snap']
    userId ="aa"

    filename = secure_filename(file.filename)
    #craet instance
    snap = Snap(request.form['title'], request.form['mini'], filename, userId)
    db.session.add(snap)
    db.session.commit()
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    a = "b"
    return a