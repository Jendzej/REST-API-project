"""Importing modules"""
from typing import Collection
from uuid import UUID, uuid4
import pymongo
from models import User
import payloads.constances


myclient = pymongo.MongoClient(payloads.constances.DATABASELINK)

mydb = myclient[payloads.constances.DATABASENAME]

users_data = mydb[payloads.constances.COLLECTIONNAME]


def join_user_data(user: User, collection_data=users_data):
    """POST method function"""
    data_to_join = {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "middle_name": user.middle_name,
        "gender": user.gender,
        "roles": user.roles
    }
    for data in collection_data.find({}, {"py_id":1}):
        if str(user.id) in data:
            data["py_id"] = uuid4()
        else:
            data_to_join["py_id"] = str(user.id)
    try:
        collection_data.insert_many(data_to_join)
    except:
        collection_data.insert_one(data_to_join)
    return user


def get_users(collection=users_data):
    """GET method function"""
    data_to_return = []
    for data in collection.find({}, {"_id":0}):
        data_to_return.append(data)
    return data_to_return


def get_one_user(user_id: UUID, collection=users_data):
    return user_id


def delete_users(user_id: UUID):
    """DELETE method function"""
    for data in users_data.find({}, {"_id":0}):
        if data["py_id"] == str(user_id):
            users_data.delete_one({"py_id": str(user_id)})
    return get_users()


def update_users(user_id: UUID):
    """PUT method function"""
    # for data in users_data.find():
    #     ip_str = str(user.id)
    #     if data["py_id"] == str(user.id):
    #         users_data.update_many({"py_id":ip_str},{"$set": {
    #             "first_name": user.first_name,
    #             "last_name": user.last_name,
    #             "middle_name": user.middle_name,
    #             "gender": user.gender,
    #             "roles": user.roles
    #         }})
    users_data.find({"py_id": str(user_id)})
    return get_users()
