import grpc
from concurrent import futures
import time

# import the generated classes
import todo_pb2
import todo_pb2_grpc

# File that contain main methods
import todo_func
from astroid.tests.testdata.python2.data.all import name

def get_task(db,tskid):
    for usr in db:
        if tskid == usr['taskid']:
            return usr


class TodoServicer(todo_pb2_grpc.TodosServiceServicer):
    
    def __init__(self):
        self.db = todo_func.List_database()
    
    def List(self,request,context):
        response = self.db
        if response is None or response == []:
            return todo_pb2.Empty()
        else:
            return response
        
    def Get(self,request,context):
        response = get_task(self.db, request)
        if response is None:
            return todo_pb2.Todo(id=request,title="")
        else:
            return response
        
# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_TodoServicer_to_server`
# to add the defined class to the server
todo_pb2_grpc.add_TodosServiceServicer_to_server(        
    TodoServicer(), server)

# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
