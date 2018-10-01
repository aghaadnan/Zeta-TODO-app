from flask_api import FlaskAPI
import firebase_admin
from firebase_admin import credentials,db
from firebase_admin import firestore
from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify, abort
from instance.config import app_config


def create_app(config_name):

    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    
    todo = db.reference('todolist') 

    @app.route('/todo/api/v1.0/tasks/', methods=['POST'])
    def addTodoTask():
        # data = request.get_json(silent=True)
        title = str(request.data.get('title', ''))
        description = str(request.data.get('description', ''))
        done = str(request.data.get("done", ""))
        task_desc = {
            'title': title,
            'description': description,
            'done': done
        }
        todo.push(task_desc)
        return jsonify({"successfully added":task_desc}),201

    @app.route('/todo/api/v1.0/tasks/', methods=['GET'])
    def allTodoTask():
        task_desc = todo.get(None)
        return jsonify({"allData":task_desc}),200 

    @app.route("/todo/api/v1.0/tasks/<string:id>",methods=['GET'])
    def getOneTask(id):
        task_desc = todo.child(id).get()
        if task_desc:
            return task_desc,200
        return {"todo":"todo task doesn't exist not found!!!"},404

    @app.route("/todo/api/v1.0/tasks/<string:id>",methods=['PUT'])
    def updateTodoTask(id):
        task = todo.get()
        if id in task:
            task['task_desc']=str(request.data.get('task_desc', ''))
            todo.child(id).update(task)
            return {"new values updated": task},200
        return {"todo":"todo task doesn't exist not found!!!"},404
    
    
    @app.route("/todo/api/v1.0/tasks/<string:id>",methods=['DELETE'])
    def deleteTodoTask(id):
        task_desc = todo.child(id).get()
        if task_desc:
            todo.child(id).delete()
            return {"task deleted": task_desc},200
        return {"todo":"todo task doesn't exist not found!!!"},404
    
    return app
