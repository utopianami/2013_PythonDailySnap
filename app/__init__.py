from flask import Flask, render_template, jsonify
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('home.html')


#@app.route('/json')
#def json():
#
#        #    userSnap = Snap.query.filter_by(user_id = session['user_id'])
#        #snapList = [dict(date = snap.date, title=snap.title, mini=snap.mini, img=snap.imgName) for snap in userSnap]
#        #return render_template('flow.html', snapList = snapList)
#
#    userSnap = Snap.query.all()
#    snapList = [dict(date = snap.date, title=snap.title, mini=snap.mini, img=snap.imgName) for snap in userSnap]
#    list = [
#        {'image':'http://static.inven.co.kr/image_2011/site_image/lol/dataninfo/icon/skinfull/xinzhao_splash_4.jpg', 'title': "title1", 'mini': "mine1"},
#        {'image':'http://static.inven.co.kr/image_2011/site_image/lol/dataninfo/icon/skinfull/xinzhao_splash_4.jpg', 'title': "title2", 'mini': "mine2"},
#        {'image': '/Users/YoungNamLee/git/dailySnapApp/button.png'}
#    ]
#    return jsonify(result=snapList)


#<div><img src="../static/uploads/{{snap.img}}" alt="{{snap.img}}"></div>
#    a = jsonify(image='http://static.inven.co.kr/image_2011/site_image/lol/dataninfo/icon/skinfull/xinzhao_splash_4.jpg')
 #   print type(a)
  #  return a


from app.users.views import mod as usersModule
from app.snap.views import mod as snapModule
from app.flow.views import mod as flowModule

app.register_blueprint(usersModule)
app.register_blueprint(snapModule)
app.register_blueprint(flowModule)