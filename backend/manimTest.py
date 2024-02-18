from manim import *
import imageParse

class PlotGraph(Scene):
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
        self.wait(1)

