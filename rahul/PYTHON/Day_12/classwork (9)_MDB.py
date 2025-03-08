import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["doss"]
 
mycol = mydb["customers"]

x = mycol.find({},{"_id":0,"name":0})

for i in x:
    print(i)