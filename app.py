import os
from flask import Flask, jsonify
from dotenv import load_dotenv
from flask_cors import CORS
from dbconfig import connect, connectDynamicDB

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)
print("Started")
#CORS(app, resources={r"/api/*": {"origins": "*"}})

# Example route to demonstrate accessing environment variables
@app.route('/', methods=["GET"])
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

@app.route('/home', methods=["GET"])
def home(): # Default value can be specified
    try:
        conn = connectDynamicDB()
        if conn is not None:
            Qry = "select * from user;";
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

if __name__ == '__main__':
    app.run(debug= os.getenv("DEBUG"))
