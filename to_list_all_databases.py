#mongodb://localhost:27017/

import pymongo

if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    
    all_db_name = client.list_database_names()
    print(all_db_name)