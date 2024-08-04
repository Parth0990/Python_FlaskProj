import os
from flask import Flask, jsonify
from dotenv import load_dotenv
from flask_cors import CORS
from Home.home import home_blueprint
from Login.login import login_blueprint

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)
#CORS(app, resources={r"/api/*": {"origins": "*"}})

app.register_blueprint(home_blueprint, url_prefix='/home')
app.register_blueprint(login_blueprint, url_prefix='/login')

@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"Message": str(error)})

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"Message": str(error)})

@app.errorhandler(Exception)
def handle_exception(error):
    return jsonify({"Message": str(error)})

if __name__ == '__main__':
    app.run(debug= os.getenv("DEBUG"), host='127.0.0.1', port=5545)
