import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["doss"]
 
mycol = mydb["customers"]
query = {"address":"Mountain 21"}

x = mycol.delete_one(query)

print(x.deleted_count,"documents deleted")