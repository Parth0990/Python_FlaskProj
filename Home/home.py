# admin.py
from flask import Blueprint, jsonify
from dbconfig import connect, connectDynamicDB

home_blueprint = Blueprint('admin', __name__)

@home_blueprint.route('/dashboard', methods=['GET'])
def admin_index():
    return jsonify({"message": "Welcome to the admin dashboard"})

@home_blueprint.route('/user', methods=["GET"])
def index(): # Default value can be specified
    try:
        conn = connect()
        if conn is not None:
            Qry = "select * from UserData;";
            cursor = conn.cursor(dictionary=True)
            cursor.execute(Qry)
            users = cursor.fetchall()
            return jsonify({"users": users}, {"Success": True})
        else:
            return jsonify({"Error": {"Message": "Please Verify DB Settings"}}, {"Success": False})
    except Exception as e:
        return jsonify({"Error": {"Message": str(e)}}, {"Success": False})
    finally:
        if conn is not None:
            cursor.close()
            conn.close()

@home_blueprint.route('/home', methods=["GET"])
def test1(): # Default value can be specified
    try:
        conn = connect()
        if conn is not None:
            Qry = "select * from UserData;";
            cursor = conn.cursor(dictionary=True)
            cursor.execute(Qry)
            users = cursor.fetchall()
            return jsonify({"users": users}, {"Success": True})
        else:
            return jsonify({"Error": {"Message": "Please Verify DB Settings"}}, {"Success": False})
    except Exception as e:
        return jsonify({"Error": {"Message": str(e)}}, {"Success": False})
    finally:
        if conn is not None:
            cursor.close()
            conn.close()

@home_blueprint.route('/home', methods=["GET"])
def home(): # Default value can be specified
    try:
        conn = connectDynamicDB()
        if conn is not None:
            Qry = "select * from UserData;";
            cursor = conn.cursor(dictionary=True)
            cursor.execute(Qry)
            users = cursor.fetchall()
            return jsonify({"users": users}, {"Success": True})
        else:
            return jsonify({"Error": {"Message": "Please Verify DB Settings"}}, {"Success": False})
    except Exception as e:
        return jsonify({"Error": {"Message": str(e)}}, {"Success": False})
    finally:
        if conn is not None:
            cursor.close()
            conn.close()