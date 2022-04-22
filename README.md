#REST API app

Simple api, which allows to get, create, delete and update data in MongoDatabase.

Used methods:

- **GET**
- **POST**
- **DELETE**
- **PUT**


##STARTING APP

- Run this command in app directory to run server:\
```bash
uvicorn main:app --reload
```
- If server is running, you can test app by typing following url to your browser:\
http://localhost:8000/api/v1/get\

##CONFIGURE APP
- **main.py**\
In this file you can configure functions, which are used by HTML methods, change endpoints urls and change file with database. \

