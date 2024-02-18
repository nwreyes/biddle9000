from flask import Flask, send_file, jsonify
from flask_cors import CORS
from sys import platform
import requests
# import manimTest
import openAIParser
import openAI
from manim import *

explanation = ""

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
    

    latexFormula = openAIParser.parseImage()
    args = openAI.getStuff(latexFormula)

    global explanation

    class_string = args["visualization_code"]
    explanation = args["explanation"]
    

    # Your Manim script to generate the MP4 file

    # Dictionary to capture the local variables after exec
    local_variables = {}
    
    # Execute the class definition, capturing the result in local_variables
    exec(class_string, globals(), local_variables)
    
    # Instantiate the class using the captured local variables
    equation = local_variables['Equation']()
    equation.render()

    # Return the path to the generated MP4 file
    if platform == 'darwin' or 'linux':
        return send_file('media/videos/1080p60/Equation.mp4')
    return send_file('media\\videos\\1080p60\\Equation.mp4')

@app.route('/get_explanation')
def get_explanation():
    # return explanation in body text
    global explanation
    # explanation = explanation.replace('\n', '<br/>')
    return jsonify({"explanation": explanation})

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=True for development, it :will automatically reload the server when you make changes
