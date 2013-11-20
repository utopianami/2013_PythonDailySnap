import os.path

UPLOAD_FOLDER = '/Users/YoungNamLee/git/daily/app/static/uploads'

#UPLOADS_FOLDER = os.path.realpath('.') + '/static/uploads'
SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test4.db'


ADMINS = frozenset(['youremail@yourdomain.com'])
SECRET_KEY = 'SecretKeyForSessionSigning'