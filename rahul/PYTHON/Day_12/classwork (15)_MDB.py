import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["doss"]
 
mycol = mydb["customers"]

x = mycol.delete_many({})

print(x.deleted_count,"documents deleted")