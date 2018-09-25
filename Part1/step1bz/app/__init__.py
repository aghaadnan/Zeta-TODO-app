from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify, abort

# local import
from instance.config import app_config

# initialize sql-alchemy
db = SQLAlchemy()

def create_app(config_name):
    from app.models import Tasklist
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    @app.route('/todo/api/v1.0/tasks', methods=['POST', 'GET'])
    def tasklists():
        if request.method == "POST":
            name = str(request.data.get('name', ''))
            description = str(request.data.get('description', ''))
            if name:
                tasklist = Tasklist(name=name,description=description)
                tasklist.save()
                response = jsonify({
                    'id': tasklist.id,
                    'name': tasklist.name,
                    'description':tasklist.description,
                    'date_created': tasklist.date_created,
                    'date_modified': tasklist.date_modified
                })
                response.status_code = 201
                return response
        else:
            # GET
            tasklists = Tasklist.get_all()
            results = []

            for tasklist in tasklists:
                obj = {
                    'id': tasklist.id,
                    'name': tasklist.name,
                    'description':tasklist.description,
                    'date_created': tasklist.date_created,
                    'date_modified': tasklist.date_modified
                }
                results.append(obj)
            response = jsonify(results)
            response.status_code = 200
            return response

    @app.route('/todo/api/v1.0/tasks/<int:id>', methods=['GET', 'PUT', 'DELETE'])
    def tasklist_manipulation(id, **kwargs):
     # retrieve a tasklist using it's ID
        tasklist = Tasklist.query.filter_by(id=id).first()
        if not tasklist:
            # Raise an HTTPException with a 404 not found status code
            abort(404)

        if request.method == 'DELETE':
            tasklist.delete()
            return {
            "message": "tasklist {} deleted successfully".format(tasklist.id)
            }, 200

        elif request.method == 'PUT':
            name = str(request.data.get('name', ''))
            description = str(request.data.get('description', ''))
            tasklist.name = name
            tasklist.description=description
            tasklist.save()
            response = jsonify({
                'id': tasklist.id,
                'name': tasklist.name,
                'description':tasklist.description,
                'date_created': tasklist.date_created,
                'date_modified': tasklist.date_modified
            })
            response.status_code = 200
            return response
        else:
            # GET
            response = jsonify({
                'id': tasklist.id,
                'name': tasklist.name,
                'description':tasklist.description,
                'date_created': tasklist.date_created,
                'date_modified': tasklist.date_modified
            })
            response.status_code = 200
            return response

    return app
