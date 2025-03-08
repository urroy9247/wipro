import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["doss"]
 
mycol = mydb["customers"]
query = {"address":{"$regex": "^S"}}

x = mycol.delete_many(query)

print(x.deleted_count,"documents deleted")