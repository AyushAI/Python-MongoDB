import pymongo

if __name__ == "__main__":
    print("Welcome to the MongoDB database!")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    db = client["ayush1"]
    collection = db["sample_collection1"]
    dictionary = {"name" : "AYUSH WASE", "education" : "Btech In AI"}
    
    collection.insert_one(dictionary)
