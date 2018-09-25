class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True

class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    DEBUG = True
    MONGO_URI='mongodb://imran:Abc123!@ds211588.mlab.com:11588/todoo'
    MONGO_DBNAME='todoo'

class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True
    MONGO_URI='mongodb://imran:Abc123!@ds123012.mlab.com:23012/todo'
    MONGO_DBNAME='todo'

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,

}
