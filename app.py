import os
from flask import Flask, jsonify
from dotenv import load_dotenv
from flask_cors import CORS
from dbconfig import connect, connectDynamicDB

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)
#CORS(app, resources={r"/api/*": {"origins": "*"}})

# Example route to demonstrate accessing environment variables
@app.route('/', methods=["GET"])
def index(): # Default value can be specified
    try:
        conn = connect()
        Qry = "select * from user; select * from user;";
        cursor = conn.cursor(dictionary=True)
        cursor.execute(Qry)
        users = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify({"users": users}, {"success": True})
    except Exception as e:
        return jsonify({"Error": {"Message": str(e)}})

@app.route('/home', methods=["GET"])
def home(): # Default value can be specified
    try:
        conn = connectDynamicDB()
        Qry = "select * from user; select * from user;";
        cursor = conn.cursor(dictionary=True)
        cursor.execute(Qry)
        users = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify({"users": users}, {"success": True})
    except Exception as e:
        return jsonify({"Error": {"Message": str(e)}})

if __name__ == '__main__':
    app.run(debug= os.getenv("DEBUG"))
