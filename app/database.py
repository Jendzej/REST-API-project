"""Importing modules"""
from uuid import UUID, uuid4
import pymongo
from models import User


myclient = pymongo.MongoClient(
"mongodb+srv://admin:admin@databaseapi.yfjsz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
)

mydb = myclient["api_database"]

users_data = mydb["Users data"]


def join_user_data(user: User, collection_data=users_data):
    """POST method function"""
    data_to_join = {}
    data_to_join["first_name"] = user.first_name
    data_to_join["last_name"] = user.last_name
    data_to_join["middle_name"] = user.middle_name
    data_to_join["gender"] = user.gender
    data_to_join["roles"] = user.roles
    for data in users_data.find({}, {"py_id":1}):
        if str(user.id) in data:
            data["py_id"] = uuid4()
        else:
            data_to_join["py_id"] = str(user.id)
    try:
        collection_data.insert_many(data_to_join)
    except:
        collection_data.insert_one(data_to_join)
    return get_users()


def get_users(collection=users_data):
    """GET method function"""
    data_to_return = []
    for data in collection.find({}, {"_id":0}):
        data_to_return.append(data)
    return data_to_return


def delete_users(user_id: UUID):
    """DELETE method function"""
    for data in users_data.find({}, {"_id":0}):
        if data["py_id"] == str(user_id):
            users_data.delete_one({"py_id": str(user_id)})
    return get_users()


def update_users(user: User):
    """PUT method function"""
    for data in users_data.find():
        ip_str = str(user.id)
        if data["py_id"] == str(user.id):
            users_data.update_many({"py_id":ip_str},{"$set": {
                "first_name": user.first_name,
                "last_name": user.last_name,
                "middle_name": user.middle_name,
                "gender": user.gender,
                "roles": user.roles
            }})
    return get_users()
