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
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


height = 200

class PongGame(Widget):
    pass
# The GUI made


    

#Returns the GUI?
class PongApp(App):
    def build(self):
        return PongGame()
    
def confirm_close(instance):
    content = BoxLayout(orientation='vertical')
    content.add_widget(Label(text='Are you sure you want to close the application? If you do you definitely get pegged'))

    # Create "Yes" button to close the app
    yes_button = Button(text='Yes', size_hint=(1, None), height=40)
    yes_button.bind(on_press=close_app)
    content.add_widget(yes_button)

    # Create "No" button to cancel
    no_button = Button(text='No', size_hint=(1, None), height=40)
    content.add_widget(no_button)

    # Create Popup
    popup = Popup(title='Confirmation', content=content, size_hint=(None, None), size=(300, 200))
    popup.open()

    # Bind "No" button to dismiss the popup
    no_button.bind(on_press=popup.dismiss)

def close_app(instance):
    App.get_running_app().stop()

class BackgroundApp(App):
    def build(self):
        root = FloatLayout()  # Switch this to whatever png we need
        bg_image = Image(source='TacSlides/GUIS/firewatch.png', allow_stretch=True, keep_ratio=False)
        close_button = Button(text='Close', size_hint=(0.2, 0.1), pos_hint={'right': 1, 'top': 1})
        close_button.bind(on_press=confirm_close)

        # Add the Image and Button widgets to the root widget
        root.add_widget(bg_image)
        root.add_widget(close_button)
        return root    

    


#main ruins the GUI
if __name__ == '__main__':
    PongApp().run()
    BackgroundApp().run()
