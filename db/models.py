from dbutils import get_db_config, get_db_connection
from datetime import datetime
from pytz import timezone
import json

class User:

    def __init__(self, id_, first_name, last_name,
                 email, is_admin, date_created):
        self.id = id_
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.date_created = date_created

    def to_json(self):
        features = {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "date_created": str(self.date_created)
        }
        return json.dumps(features)

    def __str__(self):
        return (
            "{} {}:\n"
            "\temail: {}\n"
            "\tcreated on: {}"
            .format(self.first_name,
                    self.last_name,
                    self.email,
                    self.date_created)
            )

class UserDAO:

    @staticmethod
    def insert_user(first_name, last_name, email):
        cnx, cursor = get_db_connection(*get_db_config())
        cmd = (
            "INSERT INTO users "
            "(first_name, last_name, email, is_admin, date_created) "
            "VALUES (\'{}\', \'{}\', \'{}\', "
            "FALSE, CURDATE())".format(first_name,
                                       last_name,
                                       email))
        cursor.execute(cmd)
        cnx.commit()

    @staticmethod
    def get_user(id):
        cnx, cursor = get_db_connection(*get_db_config())
        cursor.execute(("SELECT "
                        "id, first_name, last_name, email, is_admin, date_created "
                        "FROM users "
                        "WHERE id={}".format(id)))
        usrs = []
        for (id_, first_name, last_name, email, is_admin, date_created) in cursor:
            usrs.append(User(id_, first_name, last_name, email, is_admin, date_created))
        return usrs[0]
