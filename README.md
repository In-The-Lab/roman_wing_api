# Roman Wing API

## General info
This will contain all the backend logic for the Roman Wing website – it's a flask app that interacts with a database.

The DB folder will have all the database queries.

The services folder will have all the functions that verify permissions, etc, then proceed to interact with the functions in the DB folder.

Finally, routes.py will have all the necessary routes, and the functions that interact with the services in the services folder.

## Installing dependencies

run `python setup.py develop`, and you should be good.

## Getting set up and all that

First of all, follow the instructions in the README in db to get mySQL all installed and set up.

Make a folder called "config", and put a file called "config.ini" inside it with your mySQL credentials. It should look something like this:
```
[MYSQL]
user=root
database=romanwing
password=<YOUR_DATABASE_PASSWORD>
host=127.0.0.1
```