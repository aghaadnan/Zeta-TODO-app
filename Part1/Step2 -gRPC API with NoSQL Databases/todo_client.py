import todo_pb2, todo_pb2_grpc, grpc

def list_task(stub):
    result = stub.List(todo_pb2.Empty())
    print(result)


def get_task(stub):
    
    ''' Get function is define in todo_server.py file to get task by id'''
    ID = todo_pb2.TodoId()
    ID.id = '2'
    tasks = stub.Get(bin(ID))
    if not tasks:
        print("NO task found against awd")
        return
    else:
        print(tasks)
    
def run():
    channel = grpc.insecure_channel('localhost:50051') 
    stub = todo_pb2_grpc.TodosServiceStub(channel)
    print("-------------- ListFeature --------------")
    list_task(stub)
    print("-------------- GetFeatures --------------")
    get_task(stub)

run()

