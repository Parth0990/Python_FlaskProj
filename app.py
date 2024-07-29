import os
from flask import Flask
from dotenv import load_dotenv
from flask_cors import CORS
from Home.home import home_blueprint

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)
#CORS(app, resources={r"/api/*": {"origins": "*"}})

app.register_blueprint(home_blueprint, url_prefix='/home')

if __name__ == '__main__':
    app.run(debug= os.getenv("DEBUG"))
