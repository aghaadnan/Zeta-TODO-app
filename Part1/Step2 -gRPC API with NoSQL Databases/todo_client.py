import todo_pb2, todo_pb2_grpc, grpc

def list_task(stub):
    result = stub.List(todo_pb2.Empty())
    print(result)


def get_task(stub):
    
    ''' Get function is define in todo_server.py file to get task by id'''
    
    tasks = stub.Get( todo_pb2.TodoId(id='2'))
    '''for now id is hardcode but will be given by user ''' 
    if not tasks:
        print("NO task found against task")
    else:
        print(tasks)
    
def run():
    channel = grpc.insecure_channel('localhost:50051') 
    stub = todo_pb2_grpc.TodosServiceStub(channel)
    print("-------------- ListTasks --------------")
    #list_task(stub)
    print("-------------- GetTasks --------------")
    get_task(stub)

run()
