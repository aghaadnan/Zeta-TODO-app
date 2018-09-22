import pymongo
from pymongo import MongoClient
import todo_pb2
MONGODB_URI = "mongodb://awais1:awais1@ds121652.mlab.com:21652/my_todo_list"

client = MongoClient(MONGODB_URI, connectTimeoutMS=30000)
db = client.get_database("my_todo_list")
user_records = db.todo


def List_database():
    records = user_records.find({})
    tsk_list = []
    mydict={}
    for tsk in records:        
        if tsk['done']==True:flag=True
        else:flag=False
        print(tsk['note'])
        task=None
        task = todo_pb2.Todo(
            id=str(tsk['taskid']),
            title=tsk['title'],
            description=tsk['note'])
        tsk_list.append(task)
    todolist = todo_pb2.TodoList()
    todolist = tsk_list
    return todolist
