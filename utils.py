from pymongo import MongoClient

def getDbHandle(dbName, host, port, username, password):
    client = MongoClient(
        host=host, 
        port=int(port), 
        username=username, 
        password=password
    )

    dbHandle = client['dbName']
    return dbHandle, client