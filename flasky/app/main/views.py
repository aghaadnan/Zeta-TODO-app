from flask_restful import Resource
from flask import jsonify, request
from app.models import todoList 
import json


class Home(Resource):
    """Root Directory"""
    def get(self):
        return{"Welcom":"SQL Todo App"},200

class AddTodoTask(Resource):
    """AddTodoTask Directory"""   
    def post(self):        
        data = request.get_json(silent=True)
        new_task = todoList(title= data['title'], description= data['description'], done= data['done']) 
        todoList.save(new_task)    
        return {'Created data successfuly ': 'yahooo!!!'} , 201

# Get task by ID
class GetTodoTask(Resource):
    """Get Todo Task by Id"""
    def get(self, num):
        id = num        
        task = todoList.query.filter_by(id=id).first()  
        if not task:
            return {'message' : 'No todo found!' }  
        data = {}                
        data["id"]=task.id
        data["title"]= task.title 
        data["description"]= task.description 
        data["done"]= bool(task.done)       
        
        return {'tasks':data}, 200

# Delete task from TODO list
class DelTodoTask(Resource):
    """Delete Todo Task By id"""
    def delete(self, num):
        _task = todoList.query.filter_by(id=num).first()
        if _task:
            todoList.delete(_task)
            response = {'status': 'task has been deleted'}
            return response,200
        else:
            return {"task": "task doesn't exist!!"}

# update task
class UpdateTodoTask(Resource):
    """Update Todo Task by ID"""
    def put(self, num):
        data = request.get_json(silent=True)
        task = todoList.query.filter_by(id=num).first()
        if not task:
            task = todoList(title=data["title"],description= data["description"],done= data["done"])
            todoList.save(task)  
            return {"Task wasn't in database so Created ":"OK Update Section"}, 201
        else:
            task.title = data['title']
            task.description = data['description']
            task.done = data['done']
            task.save()
            return {"UPDATED":"OK"}, 200    
        
# All todo Task
class AllTodoTask(Resource):
    """Get ALL todo Task """
    def get(self):
        reslt=[]
        todos = todoList.get_all()
        if todos:
            for todoz in todos:
                data= {}                    
                data["id"] = str(todoz.id), 
                data["title"]= todoz.title, 
                data["description"]= todoz.description, 
                data["done"]= bool(todoz.done)
                reslt.append(data)    
                
            return {'tasks':reslt},200
        else:
            return {'TodoList':'Todo list is empty'}, 204