
from PIL import Image 
import random
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageOps
import tkinters
from tkinter import *
from PIL import Image, ImageTk
import math
#Flush mode warslide generator idea..
refactor_factor = 5
#Have two sides. 


from tkinter import ALL, EventType



class algorithmGUI():

    def __init__(self,directory):
        self.selected = None
        self.directory = directory
        self.img = np.array(Image.open(directory))
        print(self.img.shape)
        print(self.img[1,1])
        self.mode = 0
        self.border = []

    def returnSelected(self):
        return self.selected
    def displayGUI(self):
        root = Tk()
        root.resizable(False, False)
        w = Canvas(root, width=(self.img.shape[1]*refactor_factor), height=(self.img.shape[0]*refactor_factor))
        w.pack()


        image1 = Image.open(self.directory)
        image1 = image1.resize((image1.width*refactor_factor, image1.height*refactor_factor), 0)
        image_copy = image1.resize((image1.width*refactor_factor, image1.height*refactor_factor), 0)

        test = ImageTk.PhotoImage(image1)
        w.create_image(0,0,anchor=NW,image=test)

        #opsel_image = image1.resize((image1.width*refactor_factor, image1.height*refactor_factor), 0)

        def switch_mode1():
            self.mode = 0
            print(self.mode)
        def switch_mode2():
            self.mode = 1
            print(self.mode)
        def switch_mode3():
            self.mode = 2
            print(self.mode)



        def getcoord(event):
            global Cx, Cy
            Cx, Cy = event.x, event.y
            print('X = ', Cx, '   Y=  ', Cy)
        def getcoorddivfive(event):
            global Cx, Cy
            Cx, Cy = event.x, event.y
            #print('X = ', math.ceil(Cx/refactor_factor), '   Y=  ', math.ceil(Cy/refactor_factor))
            return math.ceil(Cx/refactor_factor), math.ceil(Cy/refactor_factor)
        def updateimage(event):
            print(getcoorddivfive(event))
            click_coords = getcoorddivfive(event) # get coordinate of clicked event
            if (self.mode==1):
                self.border.append(click_coords)
                mod_img = np.array(image1)
                mod_img[click_coords[0], click_coords[1]] = [255, 255, 255]-mod_img[click_coords[0], click_coords[1]]
                for widget in root.winfo_children():
                    if type(widget) is Canvas:
                        print(widget)
                        widget.destroy()
                w = Canvas(root, width=(self.img.shape[1]*refactor_factor), height=(self.img.shape[0]*refactor_factor))
                w.pack()
                img2 = Image.fromarray(mod_img)
                test2 = ImageTk.PhotoImage(image=img2)
                w.create_image(0,0,anchor=NW,image=test2)
            if (self.mode==2):
                pass
            if (self.mode==3):
                pass






        #w.bind('<Button-1>', getcoord)
        w.bind('<Button-1>', updateimage)





        modeDisplay = Toplevel()
        B5 = Button(modeDisplay, text ="Region Select", command = switch_mode1)
        B5.pack()
        B6 = Button(modeDisplay, text ="Slide Origin", command = switch_mode2)
        B6.pack()
        B7 = Button(modeDisplay, text ="Start process", command = switch_mode3)
        B7.pack()







        modeDisplay.mainloop()


