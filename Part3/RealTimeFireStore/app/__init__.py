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
        data = request.get_json(silent=True)
        task = {
            'title': data['title'],
            'description': data['description'],
            'done':data["done"]
        }
        todo.push(task)
        return jsonify({"successfully added":task}),201

    @app.route('/todo/api/v1.0/tasks/', methods=['GET'])
    def allTodoTask():
        data = todo.get(None)
        return jsonify({"allData":data}),200 

    @app.route("/todo/api/v1.0/tasks/<string:id>",methods=['GET'])
    def getOneTask(id):
        data = todo.get()
        for key,value in data.items():
            new = {key:value}
            if id in new:
                print(new)
                return new,200
        return {"todo":"todo task doesn't exist not found!!!"},404

    @app.route("/todo/api/v1.0/tasks/<string:id>",methods=['PUT'])
    def updateTodoTask(id):
        data = request.get_json(silent=True)
        predata = todo.get()
        if id in predata:
            todo.child(id).update(data)
            return {"new values updated": data},200
        return {"todo":"todo task doesn't exist not found!!!"},404
    
    
    @app.route("/todo/api/v1.0/tasks/<string:id>",methods=['DELETE'])
    def deleteTodoTask(id):
        dlt = todo.get()
        if id in dlt:
            todo.child(id).delete()
            return {"task deleted": dlt},200
        return {"todo":"todo task doesn't exist not found!!!"},404
    
    return app
