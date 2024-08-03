import os
from flask import Flask
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

if __name__ == '__main__':
    app.run(debug= os.getenv("DEBUG"), host='127.0.0.1', port=5545)
