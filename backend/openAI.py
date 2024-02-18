from openai import OpenAI

import config
# Create an instance of the Flask class

openai.api_key = config.API_KEY

client = OpenAI()

example_function = """class Equation(Scene):
    def construct(self):
        # Define the function and its derivative
        function_tex = r"f(x) = x^2"
        derivative_tex = r"\frac{d}{dx}f(x) = 2x"

        # Create MathTex objects to render the equations
        function_equation = MathTex(function_tex)
        derivative_equation = MathTex(derivative_tex)

        # Position the equations on the screen
        function_equation.to_edge(UP)
        derivative_equation.next_to(function_equation, DOWN, buff=0.5)

        # Show the equations on the screen
        self.play(Write(function_equation))
        self.wait(1)
        self.play(Write(derivative_equation))
        self.wait(2)"""

gpt_func_definition = {
    "type": "function",
    "function": {
        "name": "math_problem_helper",
        "description": "Creates visualizations and explanations for math problems to help students understand the problem and concepts better.",
        "parameters": {
        "type": "object",
        "properties": {
            "visualization_code": {
                "type": "string",
                "description": f"The code for the python class that creates the visualization. This code will be executed to generate the visualization. Here is an example: {example_function}",
            },
            "explanation": {
                "type": "string",
                "description": "An explanation of the math problem and the concepts involved. This will be used to help the student understand the problem better. Respond in LaTeX format, like this: $\\frac{d}{dx}f(x) = 2x$",
            }
        },
        "required": ["visualization_code", "explanation"],
        },
    }
}

response = client.chat.completions.create(
  model="gpt-4-vision-preview",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "What’s in this image?"},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
          },
        },
      ],
    }
  ],
)

print(response.choices[0])