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

class PongGame(Widget):
    pass


class PongApp(App):
    def build(self):
        return PongGame()


if __name__ == '__main__':
    PongApp().run()
