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
    mydict={}
    for tsk in records:
        tsk_list.todo.add(
            id=str(tsk['taskid']),            
            title=tsk['title'],
            description=tsk['note'],
            done=tsk['done'])
        #lis.append(task)
    #todolist = tsk_list.todo.extend(lis)
    
    #print(todolist)
    '''for usr in todolist:
        if usr.id == '1':
            print(usr)
    
    return todolist'''
    #print(tsk_list)
    #print(lis)
    return tsk_list

def Get_Database(id):
    records = user_records.find({'taskid':id})
    #return records
    tsk_list = todo_pb2.TodoList()
    mydict={}
    for tsk in records:
        tsk_list.todo.add(
            id=str(tsk['taskid']),            
            title=tsk['title'],
            description=tsk['note'],
            done=tsk['done'])
    print(tsk_list)
           
#List_database()
#Get_Database(1)  

