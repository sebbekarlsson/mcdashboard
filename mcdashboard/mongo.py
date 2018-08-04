from mcdashboard.config import config
from pymongo import MongoClient


client = MongoClient(config['mongo']['host'])


db = client[config['mongo']['db']]
