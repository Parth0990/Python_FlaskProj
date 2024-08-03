import os
import mysql.connector
from flask import jsonify 

def connect():
    try:
        _username = os.getenv('DEFUALT_Username')
        _password = os.getenv('DEFUALT_Password')
        _host = os.getenv('DEFUALT_Host')
        _dbname = os.getenv('DEFUALT_DBName') 
        print("username: " + _username + ", password: " + _password + ", host: " + _host + ", dbname: " + _dbname)
        conn = mysql.connector.connect(host=_host, user=_username, password=_password, database=_dbname)
        if conn.is_connected():
            print("Connected")
            return conn
        else:
            print("Failed")
            return None
    except Exception as e:
        print(str(e));
        return None

def connectDynamicDB():
    try:
        SetDynamicDBConfig()
        _username = os.getenv("Dynamic_Username");
        _passowrd = os.getenv("Dynamic_Password");
        _host = os.getenv("Dynamic_Host");
        _dbname = os.getenv("Dynamic_DBName");
        print("username:" + _username + ", Password: " + _passowrd + ", host: " + _host + ", dbname: " + _dbname)
        conn = mysql.connector.connect(host=_host, user=_username, password=_passowrd, database=_dbname)
        return conn
    except Exception as e:
        return None

def SetDynamicDBConfig():
    try:
        conn = connect();
        Qry = "Select * from DBSetting;";
        cursor = conn.cursor(dictionary=True)
        cursor.execute(Qry)
        dbconfig = cursor.fetchall()
        cursor.close()
        conn.close()
        os.environ["Dynamic_Username"]= dbconfig[0]["username"]
        os.environ["Dynamic_Password"]= dbconfig[0]["password"]
        os.environ["Dynamic_Host"]= dbconfig[0]["host"]
        os.environ["Dynamic_DBName"]= dbconfig[0]["dbname"]
    except Exception as e:
        return None

def SaveDataIntoTables(Qry: str, parameter: any, InsertIntoMainDb: bool):
    try:
        if InsertIntoMainDb:
            conn = connect()
            if conn is not None:

                cursor = conn.cursor(dictionary=True)
                cursor.execute(Qry, parameter)

                last_id = cursor.lastrowid
                
                if last_id > 0:
                    conn.commit()
                    return jsonify({"Message:" : "Record Inserted Successfully."}, {"Last_InsertedId": last_id})
                else:
                    conn.rollback()
                    return jsonify({"Message": "Record Failed to Insert"}, {"Last_InsertedId" : 0})
            else:
                return jsonify({"Message": "Please Verify DB Settings"})
        else:
            conn = connectDynamicDB()
            if conn is not None:

                cursor = conn.cursor(dictionary=True)
                cursor.execute(Qry, parameter)
                
                last_id = cursor.lastrowid
                
                if last_id > 0:
                    conn.commit()
                    return jsonify({"Message:" : "Record Inserted Successfully."}, {"Last_InsertedId": last_id})
                else:
                    return jsonify({"Message": "Record Failed to Insert"}, {"Last_InsertedId" : 0})
            else:
                return jsonify({"Message": "Please Verify DB Settings"})
    except Exception as e:
        return jsonify({"Message": str(e)})