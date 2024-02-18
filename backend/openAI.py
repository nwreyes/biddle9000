from openai import OpenAI
import os
import config
import sys
import json
# Create an instance of the Flask class
os.environ["OPENAI_API_KEY"] = config.OPENAI_KEY

# openai.api_key = config.API_KEY

client = OpenAI()

example_function = """class Equation(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[-3, 3],
            y_range=[-1, 8],
            axis_config={"color": BLUE},
        )

        # Original function y = x^2
        original_function = axes.plot(lambda x: x**2, color=RED)
        original_function_label = axes.get_graph_label(original_function, label='y=x^2')

        # Derivative of the function y'= 2x
        derivative_function = axes.plot(lambda x: 2*x, color=GREEN)
        derivative_function_label = axes.get_graph_label(derivative_function, label="y'=2x")

        # Display
        self.play(Create(axes), Create(original_function), Write(original_function_label))
        self.wait(1)
        self.play(Create(derivative_function), Write(derivative_function_label))
        self.wait(1)"""

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
                "description": f"The code for the python class that creates the visualization. This code will be executed to generate the visualization. The class must be named Equation. Here is an example: {example_function}",
            },
            "explanation": {
                "type": "string",
                "description": "An explanation of the math problem and the concepts involved. This will be used to help the student understand the problem better. Respond in LaTeX format, like this: $\\frac{d}{dx}f(x) = 2x$. Put equations on their own lines to make it easier to read. When an equation is on its own line, surround it with 2 dollar signs. For example: $$\\frac{d}{dx}f(x) = 2x$$.",
            }
        },
        "required": ["visualization_code", "explanation"],
        },
    }
}

tools = [gpt_func_definition]

def getStuff(text):
  completion = client.chat.completions.create(
    model="gpt-4-turbo-preview",
    messages=[
      {
        "role": "system",
        "content": "You are a math teacher and a student has asked you to help them understand the problem better. You should create a visualization and explanation to help them understand the problem and concepts better."
      },
      {
        "role": "user",
        "content": [
          {"type": "text", "text": text},
        ],
      },
    ],
    tools=tools,
    tool_choice={"type": "function", "function": {"name": "math_problem_helper"}}
  )

  args = json.loads(completion.choices[0].message.tool_calls[0].function.arguments)
  print(args, file=sys.stderr)

  return args

  

# response = client.chat.completions.create(
#   model="gpt-4-vision-preview",
#   messages=[
#     {
#       "role": "user",
#       "content": [
#         {"type": "text", "text": "What’s in this image?"},
#         {
#           "type": "image_url",
#           "image_url": {
#             "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
#           },
#         },
#       ],
#     }
#   ],
# )

# print(response.choices[0])