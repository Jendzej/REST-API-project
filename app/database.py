import pymongo
from models import User
from uuid import UUID

myclient = pymongo.MongoClient("mongodb+srv://admin:admin@databaseapi.yfjsz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

mydb = myclient["api_database"]

users_data = mydb["Users data"]


def join_user_data(user: User, collection_data=users_data):
    data_to_join = {}
    data_to_join["first_name"] = user.first_name
    data_to_join["last_name"] = user.last_name
    data_to_join["middle_name"] = user.middle_name
    data_to_join["gender"] = user.gender
    data_to_join["roles"] = user.roles
    data_to_join["py_id"] = str(user.id)
    try:
        collection_data.insert_many(data_to_join)
    except:
        collection_data.insert_one(data_to_join)
    return data_to_join["py_id"]


def get_users(collection=users_data):
    
    data_to_return = []
    for data in collection.find({}, {"_id":0}):
        data_to_return.append(data)
    return data_to_return


def delete_users(user_id: UUID):
    for data in users_data.find({}, {"_id":0}):
        if data["py_id"] == str(user_id):
            users_data.delete_one({"py_id": str(user_id)})


def update_users(user: User):
    for data in users_data.find():
        print(data["py_id"])
        if data["py_id"] == str(user.id):
            if data["first_name"] == user.first_name:
                print("Te same imiona")
            else:
                print("zmiana imienia")
                users_data.update_many({"py_id":"1f5dcdf0-7b97-4292-812e-0b82164c435a"},{"$set": {
                    "py_id": user.id,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "middle_name": user.middle_name,
                    "gender": user.gender,
                    "roles": user.roles
                }})
