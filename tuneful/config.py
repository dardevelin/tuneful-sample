class DevelopmentConfig(object):
    # either create a db with -pa or remove it from here to match yours
    DATABASE_URI = "postgresql://ubuntu:thinkful@localhost:5432/tuneful-pa"
    DEBUG = True
    UPLOAD_FOLDER = "uploads"

class TestingConfig(object):
    # either create a db with -pa or remove it from here to match yours
    DATABASE_URI = "postgresql://ubuntu:thinkful@localhost:5432/tuneful-test-pa"
    DEBUG = True
    UPLOAD_FOLDER = "test-uploads"
