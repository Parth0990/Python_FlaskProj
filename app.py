import os
from flask import Flask, jsonify
from dotenv import load_dotenv
from dbconfig import connect, connectDynamicDB

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Example route to demonstrate accessing environment variables
@app.route('/')
def index(): # Default value can be specified
    try:
        conn = connect()
        Qry = "select * from user; select * from user;";
        cursor = conn.cursor(dictionary=True)
        cursor.execute(Qry)
        users = cursor.fetchall()
    except Exception as e:
        return e
    finally:
        cursor.close()
        conn.close()
    return jsonify({'users': users})

@app.route('/home')
def home(): # Default value can be specified
    try:
        conn = connectDynamicDB()
        Qry = "select * from user; select * from user;";
        cursor = conn.cursor(dictionary=True)
        cursor.execute(Qry)
        users = cursor.fetchall()
    except Exception as e:
        return e
    finally:
        cursor.close()
        conn.close()

    return jsonify({"users": users})

if __name__ == '__main__':
    app.run()
    debug=os.getenv("DEBUG")
