from flask  import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_wtf.csrf import CSRFProtect

app = Flask(__name__,instance_relative_config=True)


#instantiate object of csrf,this will protect all your post routes against csrf and you must pass the token
csrf = CSRFProtect(app)


#to load the config
app.config.from_pyfile('config.py',silent=False)

db=SQLAlchemy(app)

#to load the routes
from attendanceapp import adminroutes,lecturerroutes,studentroutes