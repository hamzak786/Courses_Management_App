import os

class Config(object):
    SECRET_KY = os.environ.get("SECRET_KEY")

