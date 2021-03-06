from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify, abort
from flask_pymongo import PyMongo
from instance.config import app_config


def create_app(config_name):

    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')


    mongo = PyMongo(app)


    @app.route('/todo/api/v1.0/tasks/',methods=['GET'])
    def get_all_tasks():
        todo=mongo.db.Tasks

        results=[]

        for q in todo.find():

            results.append({'id':q['id'],'task_desc':q['task_desc'],'status': q['status']})

        response=jsonify(results)
        response.status_code = 200
        return response



    # get request for getting one item
    @app.route('/todo/api/v1.0/tasks/<int:id>',methods=['GET'])
    def get_one_task(id):
        todo=mongo.db.Tasks
        q=todo.find_one({'id':id})
        a=False

        if q:
            output={'id':q['id'],'task description':q['task_desc'],'status':q['status']}
            a=True

        else :
            output="no results found"


        response=jsonify(output)
        if(a==True):
            response.status_code=200
        else:
            response.status_code=404
        return response

    @app.route('/todo/api/v1.0/tasks/',methods=['POST'])
    def add_task():
        todo=mongo.db.Tasks
        task_desc=str(request.data.get('task_desc', ''))
        status=str(request.data.get('status', ''))
        id=todo.count()+1

        # id=str(request.data.get('id', ''))


        todo.insert({'id':id,'task_desc':task_desc,'status':status})
        response = jsonify({
                        'task_desc': task_desc,
                        'status': status,
                        'id':id

                    })
        response.status_code = 201
        return response

    @app.route('/todo/api/v1.0/tasks/<int:id>',methods=['DELETE'])
    def delete_task(id):
        todo=mongo.db.Tasks

        myquery={"id":id}

        todo.delete_one(myquery)
        return "task Deleted"



    @app.route('/todo/api/v1.0/tasks/<int:id>',methods=['PUT'])
    def update_task(id):
        todo=mongo.db.Tasks

        task=todo.find_one({'id':id})

        task['task_desc']=str(request.data.get('task_desc', ''))


        todo.save(task)
        return 'updated'
    return app
