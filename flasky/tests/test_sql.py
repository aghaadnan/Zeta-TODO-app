import unittest
import os, json
from app.models import todoList
from app import create_app, db
from bson.json_util import dumps
from flask import current_app, request

class testSql(unittest.TestCase):
    """This class represents the todoList test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        __tablename__ = "testdb"


        # binds the app to the current context
        # with app.app_context():
            # create all tables
            # db.create_all()

        db.create_all()
    
    def tearDown(self):
        """teardown all initialized variables."""

        db.session.remove()
        # with app.app_context():
        #     db.drop_all() 
        db.drop_all()
        self.app_context.pop()

    def datadict(self):
        return dict({ 
            'title' : 'test',
            'description' : 'testing',
            'done' : False
        })
    
   
    def test_todoList_creation(self):
        """Test API can create a todoList (POST request)"""
        res = self.client.post('/todo/api/v1.0/task/add/')
        self.assertEqual(res.status_code, 200)
        # self.assertIn('testing', str(res.data))

    def test_api_can_get_all_todoList(self):
        """Test API can get a todoList(GET request)."""
        res = self.client.post('/todo/api/v1.0/task/add/', data=self.datadict())
        self.assertEqual(res.status_code, 201)
        res = self.client.get('/todo/api/v1.0/task/all/')
        self.assertEqual(res.status_code, 200)
        self.assertIn('testing', str(res.data))

    def test_api_can_get_todoList_by_id(self):
        """Test API can get a single todoList by using it's id."""
        rv = self.client.post('/todo/api/v1.0/task/add/', data=self.datadict())
        self.assertEqual(rv.status_code, 201)
        result_in_json = json.loads(rv.data.decode('utf-8').replace("'", "\""))
        result = self.client.get(
            '/todo/api/v1.0/task/{}'.format(result_in_json['id']))
        self.assertEqual(result.status_code, 200)
        self.assertIn('str', str(result.data))

    def test_todoList_can_be_edited(self):
        """Test API can edit an existing todoList. (PUT request)"""
        rv = self.client.post('/todo/api/v1.0/add/', data=self.datadict())
        self.assertEqual(rv.status_code, 201)
        rv = self.client.put(
            '/todo/api/v1.0/task/update/1',
            data={
                "description": "testing description :-)"
            })
        self.assertEqual(rv.status_code, 200)
        results = self.client.get('/todo/api/v1.0/task/1')
        self.assertIn('testing description', str(results.data))

    def test_todoList_deletion(self):
        """Test API can delete an existing todoList. (DELETE request)."""
        rv = self.client.post('/todo/api/v1.0/add/',data=json.dumps(self.datadict()))
        self.assertEqual(rv.status_code, 201)
        res = self.client.delete('/todo/api/v1.0/task/delete/1')
        self.assertEqual(res.status_code, 200)
        # Test to see if it exists, should return a 404
        result = self.client.get('/todo/api/v1.0/task/1')
        self.assertEqual(result.status_code, 404)

    
    def test_connection(self):
        self.assertTrue(current_app.config["TESTING"]) 



# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
