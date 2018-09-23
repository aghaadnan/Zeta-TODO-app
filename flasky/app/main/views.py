from flask_restful import Resource
from flask import jsonify, request
from app.models import todoList 
import json


class Home(Resource):
    def get(self):
        return{"Welcom":"SQL Todo App"},200
    # Get task by ID
class AddTodoTask(Resource):
       
    def post(self):        
        data = request.get_json(silent=True)
        new_task = todoList(title= data['title'], description= data['description'], done= data['done']) 
        todoList.save(new_task)    
        return {'Created data successfuly ': 'yahooo!!!'} , 201

            
# Delete task from TODO list


# Get task by ID
class GetTodoTask(Resource):

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

    def put(self, num):
        data = request.get_json(silent=True)
        task = todoList.query.filter_by(id=num).first()
        if task is None:
            task = todoList(title=data["title"],description= data["description"],done= data["done"])
        else:
            task = todoList(
            title= data["title"],
            description = data['description'],
            done = data["done"]
            )
        
        todoList.save(task)
        return {"UPDATED":"OK"}, 200

class AllTodoTask(Resource):
    def get(self):
        reslt=[]
        todos = todoList.get_all()
        if todos:
            for todoz in todos:
                # id = json.loads(dumps(todoz['id']))
                data= {}                    
                data["id"] = str(todoz.id), 
                data["title"]= todoz.title, 
                data["description"]= todoz.description, 
                data["done"]= bool(todoz.done)
                reslt.append(data)    
                
            return {'tasks':reslt},200
        else:
            return {'TodoList':'Todo list is empty'}, 204

        
        
        

