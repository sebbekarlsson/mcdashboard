from mcdashboard.config import config
from mongoengine import connect


DEFAULT_CONNECTION = connect(config['mongo']['db'])
