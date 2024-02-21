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
from kivy.uix.button import Button


height = 200

class PongGame(Widget):
    pass
# The GUI made
def close_app(instance):
        App.get_running_app().stop()

#Returns the GUI?
class PongApp(App):
    def build(self):
        return PongGame()
    
    

class background(App):
    def build(self):
        root = FloatLayout()        #switch this to whatever png we need
        bg_image = Image(source='TacSlides/GUIS/firewatch.png', allow_stretch=True, keep_ratio=False)
        
        close_button = Button(text='Close', size_hint=(0.2, 0.1), pos_hint={'right': 1, 'top': 1})
        close_button.bind(on_press=close_app)
        root.add_widget(bg_image)
        root.add_widget(close_button)
        return root

    


#main ruins the GUI
if __name__ == '__main__':
    PongApp().run()
    background().run()
