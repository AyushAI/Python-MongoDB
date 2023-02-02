import pymongo

if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client["ayush"]
    collection = db["sample_collection"]

    #all_data = collection.find({"name":"Billie"},{"name":1, "age":1,"_id":0}) # 0 for false and 1 for true
    all_data = collection.find({"name":"Billie"},{"name":1, "age":1,"_id":0}).limit(1) #to print only one data
    for data in all_data:
        print(data)