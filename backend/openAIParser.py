from openai import OpenAI
import os 
import config
os.environ["OPENAI_API_KEY"] = config.OPENAI_KEY


client = OpenAI()

def parseImage():

    client = OpenAI()

    response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
        "role": "user",
        "content": [
            {"type": "text", "text": "The following is a screenshot of a math equation. please write the equation as a string. If the image is not of an equation, say 'this is not an equation'"},
            {
            "type": "image_url",
            "image_url": {
                "url": "https://i.redd.it/a65fiaqmyh681.jpg",#https://miro.medium.com/v2/resize:fit:640/format:webp/1*-PGZIOCgY_qbzeI_yGFO4A.png
            },
            },
        ],
        }
    ],
    )

    print("RESPONSE:"+response.choices[0].message.content)

    response = client.chat.completions.create(
    model="gpt-4-1106-preview",
    messages=[
        {
        "role": "user",
        "content": [
            {"type": "text", "text": f" Output this as latex. {response.choices[0].message.content}\n\n ONLY the equation in latex such as \int (u dv). DO NOT output anything other than the latex."}
        ],
        }
    ],
    )
    print(response.choices[0].message.content)
    value = response.choices[0].message.content.replace('{{', '{ {').replace('}}', '} }')

    #mathFunction.function = value

    return value


def explainFunction(function):
    response = client.chat.completions.create(
    model="gpt-4-1106-preview",
    messages=[
        {
        "role": "user",
        "content": [
            {"type": "text", "text": f"Given this function {function}, explain how we got its derivative and why it looks the way it looks."}
        ],
        }
    ],
    )
    print(response.choices[0].message.content)
    return response.choices[0].message.content



def parseImageBase64(base64_image):

    client = OpenAI()

    response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
        "role": "user",
        "content": [
            {"type": "text", "text": "The following is a screenshot of a math equation or matrix or similar math object. Please write the equation as a string. If it is a matrix or vector, format it as [[a, b], [c, d]]"},
            {
            "type": "image_url",
            "image_url": {
                "url": f"{base64_image}"
            },
            },
        ],
        }
    ],
    )

    print("RESPONSE:"+response.choices[0].message.content)

    # response = client.chat.completions.create(
    # model="gpt-4-turbo-preview",
    # messages=[
    #     {
    #     "role": "user",
    #     "content": [
    #         {"type": "text", "text": f" Output this as latex if possible. If it is not possible, say 'This is not an equation.' IF IT IS: {response.choices[0].message.content}\n\n ONLY the equation in latex such as \int (u dv). DO NOT output anything other than the latex."}
    #     ],
    #     }
    # ],
    # )
    # print(response.choices[0].message.content)
    value = response.choices[0].message.content.replace('{{', '{ {').replace('}}', '} }')

    #mathFunction.function = value

    return value


########

getVisPrompt = """```python
class Equation(Scene):
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

        # Display
        self.play(Create(axes), Create(original_function), Write(original_function_label))
        self.wait(1)
```

This is an example of a way of graphic functions. Given the following latex equation, make a visualization of the formula with values and ranges that make sense. Generate the python class to render it. I already have manim imported, so you don't need to include that part, and I know how to render the class, so you don't have to show me how to do that. Name the class Equation. Also, make sure the visualization is a video animation."""

# # Derivative of the function y'= 2x
# derivative_function = axes.plot(lambda x: 2*x, color=GREEN)
# derivative_function_label = axes.get_graph_label(derivative_function, label="y'=2x")

# self.wait(1)
# self.play(Create(derivative_function), Write(derivative_function_label))

def getVisualization(function):
    completion = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {
            "role": "system",
            "content": "You are a math instructor. Given a mathematical formula, question, matrix, vector, concept, or other, generate an interesting visualization that helps a student understand it.\n\nKeep the following principles in mind:\n- Visualize things using Manim classes with Python.\n- If a user only gives an equation, try to show the equation graphed, along with some other related equation, like its derivative, or illustrate the integral\n- If a user gives a matrix, show how that matrix's linear transformation would affect objects.\n- Only reply with the python formatted Manim class, no other text surrounding it, and no other python code besides the class.\n- Always name the class Equation"
            },
            {
            "role": "user",
            "content": "Can you show me a visualization for [[1, 2], [2, 1]]?"
            },
            {
            "role": "assistant",
            "content": "```python\nclass Equation(LinearTransformationScene):\n    def __init__(self):\n        LinearTransformationScene.__init__(\n            self,\n            show_coordinates=True,\n            leave_ghost_vectors=True,\n            show_basis_vectors=True,\n        )\n\n    def construct(self):\n\n        matrix = [[1, 2], [2, 1]]\n\n        matrix_tex = (\n            MathTex(\"A = \\\\begin{bmatrix} 1 & 2 \\\\\\ 2 & 1 \\\\end{bmatrix}\")\n            .to_edge(UL)\n            .add_background_rectangle()\n        )\n\n        unit_square = self.get_unit_square()\n        text = always_redraw(\n            lambda: Tex(\"Det(A)\").set(width=0.7).move_to(unit_square.get_center())\n        )\n\n        vect = self.get_vector([1, -2], color=PURPLE_B)\n\n        rect1 = Rectangle(\n            height=2, width=1, stroke_color=BLUE_A, fill_color=BLUE_D, fill_opacity=0.6\n        ).shift(UP * 2 + LEFT * 2)\n\n        circ1 = Circle(\n            radius=1, stroke_color=BLUE_A, fill_color=BLUE_D, fill_opacity=0.6\n        ).shift(DOWN * 2 + RIGHT * 1)\n\n        self.add_transformable_mobject(vect, unit_square, rect1, circ1)\n        self.add_background_mobject(matrix_tex, text)\n        self.apply_matrix(matrix)\n\n        self.wait()\n```"
            },
            {
            "role": "user",
            "content": "Can you show me a visualization for y = x^2?"
            },
            {
            "role": "assistant",
            "content": "```python\nclass Equation(Scene):\n    def construct(self):\n        # Create axes\n        axes = Axes(\n            x_range=[-3, 3],\n            y_range=[-1, 8],\n            axis_config={\"color\": BLUE},\n        )\n\n        # Original function y = x^2\n        original_function = axes.plot(lambda x: x**2, color=RED)\n        original_function_label = axes.get_graph_label(original_function, label='y=x^2')\n\n        # Derivative of the function y'= 2x\n        derivative_function = axes.plot(lambda x: 2*x, color=GREEN)\n        derivative_function_label = axes.get_graph_label(derivative_function, label=\"y'=2x\")\n\n        # Display\n        self.play(Create(axes), Create(original_function), Write(original_function_label))\n        self.wait(1)\n        self.play(Create(derivative_function), Write(derivative_function_label))\n        self.wait(1)\n```"
            },
            {
                "role": "user",
                "content": f"Can you show me a visualization for {function}?"
            }
        ],
        temperature=1,
        max_tokens=1387,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # completion = client.chat.completions.create(
    #     model="gpt-4-turbo-preview",
    #     messages=[
    #     {
    #         "role": "user",
    #         "content": [
    #         {"type": "text", "text": f"{getVisPrompt}\n\nFunction: {function}"},
    #         ],
    #     },
    #     ]
    # )

    pythonClass = parsePythonClass(completion.choices[0].message.content)

    return pythonClass


def parsePythonClass(text):
    completion = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
        {
            "role": "user",
            "content": [
            {"type": "text", "text": f"{text}\n\n---\n\nGiven the text above, return only the python class. Don't include any imports, just the class itself. Don't include any other text, just the class."},
            ],
        },
        ]
    )

    # remove first and last lines if they start with backticks
    lines = completion.choices[0].message.content.split("\n")
    if lines[0].startswith("```"):
        lines = lines[1:]
    if lines[-1].startswith("```"):
        lines = lines[:-1]

    return "\n".join(lines)

def getExplanation(function):
    completion = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
        {
            "role": "user",
            "content": [
            {"type": "text", "text": f"Given the function {function}, explain the concept behind the function and why it looks the way it does. Format the explanation in LaTeX format. For example: $\\frac{{d}}{{dx}}f(x) = 2x$. Put equations on their own lines to make it easier to read. When an equation is on its own line, surround it with 2 dollar signs. For example: $$\\frac{{d}}{{dx}}f(x) = 2x$$. Explain BRIEFLY and CONCISELY."},
            ],
        },
        ]
    )
    return completion.choices[0].message.content