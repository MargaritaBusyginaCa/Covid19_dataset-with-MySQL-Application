import mysql.connector
from db_connector import mycursor
#COMPLETED BY MARGARITA BUSYGINA
DB_NAME='covid19'
def create_database():
    mycursor.execute("CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    print("Database {} created!".format(DB_NAME))


create_database()