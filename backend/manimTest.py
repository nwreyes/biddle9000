from manim import *

# class Equation(Scene):
#     def construct(self):
#         # Define the function and its derivative
#         function_tex = r"f(x) = x^2"
#         derivative_tex = r"\frac{d}{dx}f(x) = 2x"

#         # Create MathTex objects to render the equations
#         function_equation = MathTex(function_tex)
#         derivative_equation = MathTex(derivative_tex)

#         # Position the equations on the screen
#         function_equation.to_edge(UP)
#         derivative_equation.next_to(function_equation, DOWN, buff=0.5)

#         # Show the equations on the screen
#         self.play(Write(function_equation))
#         self.wait(1)
#         self.play(Write(derivative_equation))
#         self.wait(2)

class Equation(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-3, 3],
            y_range=[-1, 9],
            axis_config={"color": BLUE},
        )

        original_func = axes.plot(lambda x: x**2, color=RED)
        original_func_label = axes.get_graph_label(original_func, label='y = x^2')

        derivative_func = axes.plot(lambda x: 2*x, color=GREEN)
        derivative_func_label = axes.get_graph_label(derivative_func, label="y' = 2x", x_val=-2, direction=UP)

        self.add(axes, original_func, original_func_label, derivative_func, derivative_func_label)