import pymongo

if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client["ayush"]
    collection = db["sample_collection"]
    
    data = collection.find_one({"name":"Billie"}) # this will find one the data in the database
    print(data)
    
    all_data = collection.find({"name":"Billie"}) # this will find all the data in the database
    for doc in all_data:
        print(doc)