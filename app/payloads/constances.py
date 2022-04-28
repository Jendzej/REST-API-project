from dotenv import load_dotenv, find_dotenv
import os


load_dotenv(find_dotenv())
print()

DATABASENAME = 'api_database'
COLLECTIONNAME = 'users_data'
DATABASELINK = f'mongodb+srv://{os.environ.get("USERNAME")}:{os.environ.get("PASSWORD")}@databaseapi.yfjsz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'