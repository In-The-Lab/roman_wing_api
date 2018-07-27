from dbutils import get_db_config, get_db_connection
from models import User

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

print(UserDAO.get_user(1))