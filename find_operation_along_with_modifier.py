import pymongo

if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["ayush"]
    collection = db["sample_collection"]

    allDocs = collection.find({"name":"AYUSH","age":{"$lte":21}}) # $lte is used as less than equal to 21
    for doc in allDocs:
        print(doc)