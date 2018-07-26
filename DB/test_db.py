from mysql.connector import connection

try:
    cnx = connection.MySQLConnection(user='root',
                                     password='dbpassword',
                                     host='127.0.0.1',
                                     database='romanwing')
    print("All connected!")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)