import os
from flask import Flask, jsonify
from dotenv import load_dotenv
from dbconfig import connect

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

if __name__ == '__main__':
    app.run()
    debug=os.getenv("DEBUG")
