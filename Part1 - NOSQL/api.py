# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 00:11:12 2018

@author: root
"""

from flask import Flask, request
from flask_restful import Resource, Api
from flask_mongoalchemy import MongoAlchemy

app = Flask(__name__)
api = Api(app)


app.config['MONGOALCHEMY_DATABASE'] = 'todo_app'
app.config['MONGOALCHEMY_CONNECTION_STRING'] = 'mongodb://furqan:qwerty1@ds235251.mlab.com:35251/todo_app'

db = MongoAlchemy(app)

## DATABASE COLLECTION
class TDA(db.Document):
  
  id = db.IntField()
  title = db.StringField()
  desc = db.StringField()
  done = db.BoolField()


class TODO(Resource):
    def get(self):
        task = {
            'id' : 1,
            'title' : 'my task',
            'desc' : 'Jo bi hay',
            'done' : 'true'
        }
        return task

# Adding new Task
class AddTodoTask(Resource):
    def post(self):

      task_json = request.get_json()
      
      ##COUNTING NUMBER OF DOCUMENTS IN DATABASE
      _count = TDA.query.count()
      _count=_count+1
      
      ##SAVING INTO DATABASE
      new_task = TDA(id=_count, title=task_json['title'], desc= task_json['desc'], done=False)
      new_task.save()
      return {"Task added:": {"id" : _count, "title": task_json['title'], "desc" : task_json['desc'], "done": False }}, 201

# Get task by ID
class GetTodoTask(Resource):
    def get(self, num):
      
      todo = TDA.query.filter_by(id=num).first()
  
      if not todo:
        return {"message": "Somethings seems wrong, no todo againest id"}
      
      task_data={}
      task_data['id']=todo.id
      task_data['title']=todo.title
      task_data['desc']=todo.desc
      task_data['done']=todo.done  
    
      return { 'task': task_data }

# Delete task from TODO list
class DelTodoTask(Resource):
    def delete(self, num):
      
      ## DELETING DOCUMENT PROVIDED WITH ID
      todo = TDA.query.filter_by(id = num).first()
  
      if not todo:
        return {"message": "Somethings seems wrong, no todo againest id"}
      
      todo.remove()
      
      return {'Deleted Task:': num}

# update task
class UpdateTodoTask(Resource):
    def put(self, num):
      task_json = request.get_json()
      
      todo = TDA.query.filter_by(id = num).first()
      
      if not todo:
        return {"message": "Somethings seems wrong, no todo againest id"}
      
      todo.title = task_json['title']
      todo.desc = task_json['desc']
      todo.done = task_json['done']
      todo.save()
    
      return {'Updated task:': task_json}

class AllTodoTask(Resource):
    def get(self):
              
      todos = TDA.query.all()
      
      output=[]      
      for q in todos:
        task_data={}
        task_data['id']=q.id
        task_data['title']=q.title
        task_data['description']=q.desc
        task_data['done']=q.done
        output.append(task_data)
      
      return {'All tasks:': output}

api.add_resource(TODO, "/TODO/api/v1.0/")
api.add_resource(AddTodoTask, "/TODO/api/v1.0/task/add")
api.add_resource(GetTodoTask, "/TODO/api/v1.0/task/<int:num>")
api.add_resource(DelTodoTask, "/TODO/api/v1.0/task/delete/<int:num>")
api.add_resource(UpdateTodoTask, "/TODO/api/v1.0/task/update/<int:num>")
api.add_resource(AllTodoTask, "/TODO/api/v1.0/task/all")
if __name__ == '__main__':
    #app.run(debug=True)
    app.run(debug=True, port=11111)