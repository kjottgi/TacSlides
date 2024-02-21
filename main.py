import random
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageOps
import tkinter
from tkinter import *
from PIL import Image, ImageTk
import math
import os
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image


height = 200

class PongGame(Widget):
    pass
# The GUI made


#Returns the GUI?
class PongApp(App):
    def build(self):
        return PongGame()
    

class background(App):
    def build(self):
        # Create a FloatLayout as the root widget
        root = FloatLayout()

        # Create an Image widget as the background
        bg_image = Image(source='TacSlides/GUIS/firewatch.png', allow_stretch=True, keep_ratio=False)

        # Add the Image widget to the root widget
        root.add_widget(bg_image)

        return root

    


#main ruins the GUI
if __name__ == '__main__':
    PongApp().run()
    background().run()
