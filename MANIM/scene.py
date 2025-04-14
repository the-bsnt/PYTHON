from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(BLACK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen
