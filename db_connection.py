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


def dataUjiScore(score):
    db = getDbConnection()
    collection = db['logs']
    
    pipeline = [
        { '$unwind': '$keyValueLabels' },
        { '$match': { 'keyValueLabels': { '$in': [score] } } },
        { '$project': { 'keyValueLabels': 1, '_id': 0 } }
    ]
    
    result = collection.aggregate(pipeline)
    return list(result)

def countDataUjiScore(score):
    db = getDbConnection()
    collection = db['logs']
    
    pipeline = [
        { '$unwind': '$keyValueLabels' },
        { '$match': { 'keyValueLabels': { '$in': [score] } } },
        { '$count': 'count' }
    ]
    
    result = collection.aggregate(pipeline)
    count_result = list(result)
    
    if count_result:
        return count_result[0]['count']
    else:
        return 0