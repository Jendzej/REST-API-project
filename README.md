<h1>REST API app</h1>

Simple api, which allows to get, create, delete and update data in MongoDatabase.

Used methods:

- **GET**
- **POST**
- **DELETE**
- **PUT**


<h3>STARTING APP</h3>

- Run this command in app directory to run server:
```bash
uvicorn main:app --reload
```
- If server is running, you can test app by typing following url to your browser:\
http://localhost:8000/api/v1/get

<h3>CONFIGURE APP</h3>
<h5>main.py</h5>
In this file you can configure functions, which are used by HTML methods, change endpoints urls and change file with database.\
*example:*
```python
[...]
@app.get("/url_path/")
async def function():
    """example of GET endpoint with url 'localhost:8000/url_path/' which returns data_to_return """
    return data_to_return
```