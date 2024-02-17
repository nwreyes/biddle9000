from manim import *

class Equation(Scene):
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
        self.wait(2)

