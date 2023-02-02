import pymongo

if __name__ == '__main__':
    print("Welcome to the MongoDB Python Tutorial")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    db = client["ayush"]
    collection = db["sample_collection"]
    list_dic = [
        {"name": "Ayush", "age": 21, "gender": "Male", "email" : "ayushwase28@gmail.com"},
        {"name": "Billie","age": 21, "gender":"Female", "email":"ellish21@gmail.com"},
        {"name": "Ava", "age":21, "gender":"Female","email":"ava001@gmail.com"},
        {"name": "Myself", "age" : "infinity", "gender": "Male","email":"myself@gmail.com"}
    ]
    collection.insert_many(list_dic)
