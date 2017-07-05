Market API
----------

To setup this application you should create virtualenv and run following commands:
```sh
$ pip install -r requirements.txt
$ ./manage.py migrate
$ ./manage.py runserver
```

API Examples
------------

To create new product you should make POST request to http://localhost:8000/products/
with payload:
```json
{
  "name": "product name",
  "description": "product description"
}
```

To vote for a product you should make POST request to http://localhost:8000/votes/
with payload:
```json
{
  "product": "product id",
  "value": "rating value in range 0-5"
}
```

For more info about API implementation please visit http://localhost:8000/


Also you can access products data via admin panel.
Default admin credentials is ```admin:admin```
