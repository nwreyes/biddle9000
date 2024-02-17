from flask import Flask, send_file
from flask_cors import CORS
import requests
import manimTest

# Create an instance of the Flask class
app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes


# Define a route and the associated function to handle requests to that route
@app.route('/')
def hello_world():
    return 'Hello, World!'


# Define a route and the associated function to handle requests to that route
@app.route('/generate_video')
def generate_video():
    # Your Manim script to generate the MP4 file
    scene = manimTest.SquareToCircle()
    scene.render()

    # Return the path to the generated MP4 file
    return send_file('media\\videos\\1080p60\\SquareToCircle.mp4')



# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=True for development, it will automatically reload the server when you make changes
