from flask import Flask
from flask_cors import CORS
import requests


# Create an instance of the Flask class
app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes


# Define a route and the associated function to handle requests to that route
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=True for development, it will automatically reload the server when you make changes
