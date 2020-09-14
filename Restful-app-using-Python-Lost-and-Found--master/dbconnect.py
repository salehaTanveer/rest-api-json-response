from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
import pymysql
from config import SQL_USER, SQL_HOST,SQL_PASS, SQL_DB
from flask_script import Manager
from flask_migrate import Migrate , MigrateCommand



#init aap
app = Flask(__name__)
app.secret_key = "login key"


#database
db_url= 'mysql+pymysql://' + SQL_USER + ':' + SQL_PASS + '@' + SQL_HOST + '/' + SQL_DB
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
#initdb
db = SQLAlchemy(app)
#init marshmallow
ma = Marshmallow(app)

# Import database models with app context
with app.app_context():
  from dbconnect import *

#db migrate
migrate = Migrate(app , db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


#Run Server
if __name__== '__main__':
    manager.run()
    app.run(debug=True)



