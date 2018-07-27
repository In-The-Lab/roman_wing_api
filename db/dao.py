from .dbutils import get_db_config, get_db_connection
from .models import User

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
            usr = User(id_, first_name, last_name, email,
                             is_admin, date_created)
            usrs.append(usr)
        if len(usrs) == 0:
            return None
        return usrs[0]

    @staticmethod
    def get_user_by_email(email):
        cnx, cursor = get_db_connection(*get_db_config())
        cmd = (("SELECT "
                        "id, first_name, last_name, email, is_admin, date_created "
                        "FROM users "
                        "WHERE email=\'{}\'".format(email)))
        cursor.execute(cmd)
        usrs = []
        for (id_, first_name, last_name, email, is_admin, date_created) in cursor:
            usr = User(id_, first_name, last_name, email,
                             is_admin, date_created)
            usrs.append(usr)
        if len(usrs) == 0:
            return None
        return usrs[0]

class AuthDAO:

    @staticmethod
    def insert_hash(user_id, hash_):
        cnx, cursor = get_db_connection(*get_db_config())
        cmd = (
            "INSERT INTO user_auth "
            "(hash, user_id) "
            "VALUES (\'{}\', \'{}\')".format(hash_.decode('utf8'), user_id)
            )
        print(cmd)
        cursor.execute(cmd)
        cnx.commit()

    @staticmethod
    def get_hash(user_id):
        cnx, cursor = get_db_connection(*get_db_config())
        cmd = "SELECT hash from user_auth WHERE user_id={}".format(user_id)
        print(cmd)
        cursor.execute(cmd)
        hashes = []
        for (hash_) in cursor:
            print(hash_)
            hashes.append(hash_)
        return hashes[0][0].encode('utf-8')