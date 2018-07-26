# Roman Wing API

## General info
This will contain all the backend logic for the Roman Wing website – it's a flask app that interacts with a database.

The DB folder will have all the database queries.

The services folder will have all the functions that verify permissions, etc, then proceed to interact with the functions in the DB folder.

Finally, routes.py will have all the necessary routes, and the functions that interact with the services in the services folder.

# Installing dependencies

run `python setup.py develop`, and you should be good.