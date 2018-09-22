import grpc
from concurrent import futures
import time

# import the generated classes
import todo_pb2
import todo_pb2_grpc

# File that contain main methods
import todo_func
from astroid.tests.testdata.python2.data.all import name

def get_user(db,tskid):
    for usr in db:
        if tskid == usr['userid']:
            return usr


class TodoServicer(todo_pb2_grpc.TodosServiceServicer):
    
    def __init__(self):
        self.db = todo_func.List_database()
    
    def List(self,request,context):
        response = todo_pb2.TodoList
        response.todo = db
        if response is None:
            return todo_pb2.Todo(id=request,title="")
        else:
            return response
        
    def Get(self,request,context):
        response = get_user(self.db, request)
        if response is None:
            return todo_pb2.Todo(id=request,title="")
        else:
            return response        