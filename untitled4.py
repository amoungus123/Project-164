# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 19:38:05 2022

@author: pulle
"""

from tkinter import *

root = Tk()
root.title("Project 164")
root.geometry("500x500")
root.configure(background="lavender")

name = Label(root, font=("courier",25,"bold"), bg="lavender", text="Project 164")
label_planet_image = Label(root, bg="gold2", highlightthickness=5, borderwidth=2, relief=SOLID)


def PlanetInfo():
    print("hi")
    
btn = Button(root, text="Open Image" , command=PlanetInfo)
btn.place(relx=0.5, rely=0.18, anchor=CENTER)

btn2 = Button(root, text="Rotate Image" , command=PlanetInfo)
btn2.place(relx=0.5, rely=0.8, anchor=CENTER)

name.place(relx=0.5, rely=0.05, anchor=CENTER)
label_planet_image.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()