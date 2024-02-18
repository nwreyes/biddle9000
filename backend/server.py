from flask import Flask, send_file
from flask_cors import CORS
from sys import platform
import requests
# import manimTest
from manim import *

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

    # Class definition as a string
    class_string = """class Equation(Scene):
        def construct(self):
            function_tex = r"f(x) = x^2"
            derivative_tex = r"\\frac{d}{dx}f(x) = 2x"

            function_equation = MathTex(function_tex)
            derivative_equation = MathTex(derivative_tex)

            function_equation.to_edge(UP)
            derivative_equation.next_to(function_equation, DOWN, buff=0.5)

            self.play(Write(function_equation))
            self.wait(1)
            self.play(Write(derivative_equation))
            self.wait(2)"""

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



# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=True for development, it :will automatically reload the server when you make changes
