from flask import Flask ,request,jsonify
from flask_restful import Resource, Api
from app import create_app
app = create_app("default")

api = Api(app)

from app.main.views import GetTodoTask,AddTodoTask,DelTodoTask,UpdateTodoTask ,AllTodoTask,Home
api.add_resource(Home,"/")
api.add_resource(GetTodoTask, "/todo/api/v1.0/task/<int:num>")
api.add_resource(AddTodoTask, "/todo/api/v1.0/task/add/")
api.add_resource(DelTodoTask, "/todo/api/v1.0/task/delete/<int:num>")
api.add_resource(UpdateTodoTask, "/todo/api/v1.0/task/update/<int:num>")
api.add_resource(AllTodoTask, "/todo/api/v1.0/task/all/")

@app.cli.command() 
def test():    
    """Run the unit tests."""
    import unittest    
    tests = unittest.TestLoader().discover('tests_sql')    
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    app.run(debug=True)