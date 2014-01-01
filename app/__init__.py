from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy




app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)


@app.route('/')
def index():
	return render_template('home.html')

@app.route('/test')
def test():
	return 'alertMessageId()'


from app.users.views import mod as usersModule
from app.snap.views import mod as snapModule
from app.flow.views import mod as flowModule

app.register_blueprint(usersModule)
app.register_blueprint(snapModule)
app.register_blueprint(flowModule)
