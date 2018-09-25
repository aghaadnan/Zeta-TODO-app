import unittest
import os
import json
from app import create_app, db

class TasklistTestCase(unittest.TestCase):
    """This class represents the tasklist test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.tasklist = {'name': 'Go to Borabora for vacation'}

        # binds the app to the current context
        with self.app.app_context():

            # create all tables
            db.create_all()

    def test_tasklist_creation(self):
        """Test API can create a tasklist (POST request)"""
        res = self.client().post('/todo/api/v1.0/tasks', data=self.tasklist)
        self.assertEqual(res.status_code, 201)
        self.assertIn('Go to Borabora', str(res.data))

    def test_api_can_get_all_tasklists(self):
        """Test API can get a tasklist (GET request)."""
        res = self.client().post('/todo/api/v1.0/tasks', data=self.tasklist)
        self.assertEqual(res.status_code, 201)
        res = self.client().get('/todo/api/v1.0/tasks')
        self.assertEqual(res.status_code, 200)
        self.assertIn('Go to Borabora', str(res.data))

    def test_api_can_get_tasklist_by_id(self):
        """Test API can get a single tasklist by using it's id."""
        rv = self.client().post('/todo/api/v1.0/tasks', data=self.tasklist)
        self.assertEqual(rv.status_code, 201)
        result_in_json = json.loads(rv.data.decode('utf-8').replace("'", "\""))
        result = self.client().get(
            '/todo/api/v1.0/tasks/{}'.format(result_in_json['id']))
        self.assertEqual(result.status_code, 200)
        self.assertIn('Go to Borabora', str(result.data))

    def test_tasklist_can_be_edited(self):
        """Test API can edit an existing tasklist. (PUT request)"""
        rv = self.client().post(
            '/todo/api/v1.0/tasks',
            data={'name': 'Eat, pray and love'})
        self.assertEqual(rv.status_code, 201)
        rv = self.client().put(
            '/todo/api/v1.0/tasks/1',
            data={
                "name": "Dont just eat, but also pray and love :-)"
            })
        self.assertEqual(rv.status_code, 200)
        results = self.client().get('/todo/api/v1.0/tasks/1')
        self.assertIn('Dont just eat', str(results.data))

    def test_tasklist_deletion(self):
        """Test API can delete an existing tasklist. (DEL request)."""
        rv = self.client().post(
            '/todo/api/v1.0/tasks',
            data={'name': 'Eat, pray and love'})
        self.assertEqual(rv.status_code, 201)
        res = self.client().delete('/todo/api/v1.0/tasks/1')
        self.assertEqual(res.status_code, 200)
        # Test to see if it exists, should return a 404
        result = self.client().get('/todo/api/v1.0/tasks/1')
        self.assertEqual(result.status_code, 404)

    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
