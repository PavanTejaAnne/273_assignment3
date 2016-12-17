from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)

DATABASE = 'Test'
PASSWORD = 'pavan'
USER = 'root'
HOSTNAME = 'Base3'


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%s:%s@%s/%s'%(USER, PASSWORD, HOSTNAME, DATABASE)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate_obj = Migrate(app, db)
manager_obj = Manager(app)

manager_obj.add_command('db', MigrateCommand)

class Expenses(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    category = db.Column(db.String(100))
    description = db.Column(db.String(100))
    link = db.Column(db.String(100))
    estimated_costs = db.Column(db.String(100))
    submit_date = db.Column(db.String(100))
    decision_date = db.Column(db.String(100))
    status = db.Column(db.String(100))

    def __init__(self, id, name, email, category, description, link, estimated_costs, submit_date, status, decision_date):
        self.id = id
        self.name = name
        self.email = email
        self.category = category
        self.description = description
        self.link = link
        self.estimated_costs = estimated_costs
        self.submit_date = submit_date
        self.decision_date = decision_date
        self.status = status
def createdb():
    import sqlalchemy
    engine = sqlalchemy.create_engine('mysql://%s:%s@%s'%(USER, PASSWORD, HOSTNAME)) # connect to server
    engine.execute("CREATE DATABASE IF NOT EXISTS %s "%(DATABASE)) #create db

if __name__ == '__main__':
	manager_obj.run()



