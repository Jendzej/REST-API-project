import pymongo

def join_data(tags: list, data: list, collection):
    data_to_join = []
    loop_num = 0
    for tag in tags:
        data_to_join.append({f"{tag}":f"{data[loop_num]}"})
        loop_num+=1
    try:
        collection.insert_one(data_to_join)
    except:
        collection.insert_many(data_to_join)

myclient = pymongo.MongoClient("mongodb+srv://admin:admin@databaseapi.yfjsz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

mydb = myclient["mydatabase"]

collection1 = mydb["users"]

mylist = [
  { "_id": 1, "name": "John", "address": "Highway 37"},
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
  { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "_id": 5, "name": "Michael", "address": "Valley 345"},
  { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "_id": 8, "name": "Richard", "address": "Sky st 331"},
  { "_id": 9, "name": "Susan", "address": "One way 98"},
  { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "_id": 12, "name": "William", "address": "Central st 954"},
  { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]

put_data = collection1.insert_many(mylist)

print(put_data.inserted_ids)