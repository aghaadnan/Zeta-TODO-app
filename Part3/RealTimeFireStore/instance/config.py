class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    DEBUG = True
    if (not len(firebase_admin._apps)):
        cred = credentials.Certificate("E:/saylani/python/team-todo-app/ZetaTODOapp/Part3/RealTimeFireStore/todo-test-zeta.json")
        firebase_admin.initialize_app(cred,options={'databaseURL': "https://todo-test-zeta.firebaseio.com"})
class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True
    if (not len(firebase_admin._apps)):
        cred = credentials.Certificate("E:/saylani/python/team-todo-app/ZetaTODOapp/Part3/RealTimeFireStore/instance/ServiceAccountKey.json")
        firebase_admin.initialize_app(cred,options={'databaseURL': "https://todo-zeta.firebaseio.com"})

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,

}
