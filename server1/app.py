from flask import Flask, jsonify
from flask import request
from model import db
from model import createdb
from model import Expenses
from sqlalchemy.exc import IntegrityError
import json

app = Flask(__name__)
createdb()
db.create_all()

@app.route('/')
def index():
	return 'Hello World\n'

@app.route('/v1/expenses/<int:expense_id>', methods= ['GET', 'PUT', 'DELETE'])
def expense(expense_id):
    db_obj = Expenses.query.filter_by(id=expense_id).first_or_404()
    if request.method == 'GET':
        return jsonify({'id' : db_obj.id,
                           'name': db_obj.name,
                           'email': db_obj.email,
                           'category': db_obj.category,
                           'description': db_obj.description,
                           'link': db_obj.link,
                           'estimated_costs': db_obj.estimated_costs,
                           'submit_date': db_obj.submit_date,
                           'decision_date': db_obj.decision_date,
                           'status': db_obj.status
                        })

    if request.method == 'PUT':
           json_obj = request.get_json(force=True)
           db_obj.estimated_costs = json_obj['estimated_costs']
           db.session.commit()
           return jsonify({'status': True}), 202
    if request.method == 'DELETE':
        db.session.delete(db_obj)
        db.session.commit()
        return jsonify({'status': True}), 204

@app.route('/v1/expenses', methods=['POST'])

def insert_to_expense():
    try:
        json_obj = request.get_json(force=True)
        db_obj = Expenses(id=json_obj['id'], name=json_obj['name'], email=json_obj['email'], category=json_obj['category'],
                        description=json_obj['description'], link=json_obj['link'],
                        estimated_costs=json_obj['estimated_costs'], submit_date=json_obj['submit_date'],
                        status="Pending", decision_date= "")
        db.session.add(db_obj)
        db.session.flush()
        db.session.commit()

        return jsonify({'id': db_obj.id,
                        'name': db_obj.name,
                        'email': db_obj.email,
                        'category': db_obj.category,
                        'description': db_obj.description,
                        'link': db_obj.link,
                        'estimated_costs': db_obj.estimated_costs,
                        'submit_date': db_obj.submit_date,
                        'status': db_obj.status,
                        'decision_date': db_obj.decision_date
                        }), 201
    except IntegrityError as e:
        db.session.rollback()
        return json.dumps({'status': False}, e)

if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0',port=5001)

