import os
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
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

@mod.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['snap']
        userId = session['user_id']


        if 1 ==1:
            filename = secure_filename(file.filename)
            #craet instance
            snap = Snap(request.form['title'], request.form['mini'], filename, userId)
            db.session.add(snap)
            db.session.commit()
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))            
            
            return redirect(url_for('flow.flows'))

    return redirect('/')