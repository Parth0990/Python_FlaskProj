import os
import mysql.connector

def connect():
    try:
        _username = os.getenv('DEFUALT_Username')
        _password = os.getenv('DEFUALT_Password')
        _host = os.getenv('DEFUALT_Host')
        _dbname = os.getenv('DEFUALT_DBName') 
        conn = mysql.connector.connect(host=_host, user=_username, password=_password, database=_dbname)
        if conn.is_connected():
            return conn
        else:
            return "Verify Db Config"
    except Exception as e:
        print(e)
    finally:
        print("end")