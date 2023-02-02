import pymongo

if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["ayush"]
    collection = db["sample_collection"]

    #Previous = {"email":"myself@example.com"}
    Previous = {"name":"Myself"}
    Next = {"$set":{"email":"myself28@gmail.com"}}

    collection.update_one(Previous, Next)
