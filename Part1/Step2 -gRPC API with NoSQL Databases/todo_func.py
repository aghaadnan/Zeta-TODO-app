import pymongo
from pymongo import MongoClient
import todo_pb2
MONGODB_URI = "mongodb://awais1:awais1@ds121652.mlab.com:21652/my_todo_list"

client = MongoClient(MONGODB_URI, connectTimeoutMS=30000)
db = client.get_database("my_todo_list")
user_records = db.todo


def List_database():
    records = user_records.find({})
   
    tsk_list = todo_pb2.TodoList()

    for tsk in records:
        tsk_list.todo.add(
            id=str(tsk['taskid']),            
            title=tsk['title'],
            description=tsk['note'],
            done=tsk['done'])
    return tsk_list

def Get_Database(id):
    records = user_records.find({'taskid':int(id)})
    #return records
    tsk_list = todo_pb2.TodoList()
    
    for tsk in records:
        tsk_list.todo.add(
            id=str(tsk['taskid']),            
            title=tsk['title'],
            description=tsk['note'],
            done=tsk['done'])
    '''tsk_list obj doesnot print any "done" field when we return full obj but you can explicitly print it '''
    ###print(tsk_list.todo[0].done) 
    return tsk_list

#Get_Database('1')


