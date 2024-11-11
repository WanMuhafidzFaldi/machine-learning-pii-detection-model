import os
from pymongo import MongoClient

def getDbConnection():
    mongo_uri = os.getenv('MONGO_URI')
    database_name = os.getenv('MONGO_DATABASE_NAME')
    
    client = MongoClient(mongo_uri)
    db = client[database_name]
    return db

def loadDataUji():
    db = getDbConnection()
    collection = db['logs']
    data = collection.find({})

    return data