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
    conn = connect()
    Qry = "select * from user; select * from user;";
    cursor = conn.cursor(dictionary=True)
    cursor.execute(Qry)
    users = cursor.fetchall()

    return jsonify({'users': users})

@app.route('/home')
def home(): # Default value can be specified
    conn1 = connectDynamicDB()
    Qry = "select * from user; select * from user;";
    cursor1 = conn1.cursor(dictionary=True)
    cursor1.execute(Qry)
    users = cursor1.fetchall()

    return jsonify({"users": users})

if __name__ == '__main__':
    app.run()
    debug=os.getenv("DEBUG")
