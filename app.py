from tkinter import *
import tkinter
import os


top = tkinter.Tk()
top.geometry("800x600")

Label(top, text="Steinanzahl").pack()
stone_count = Entry(top)
stone_count.pack()

Label(top, text="Steinhöhe").pack()
stone_height = Entry(top)
stone_height.pack()

Label(top, text="Steinlänge").pack()
stone_length = Entry(top)
stone_length.pack()

Label(top, text="Steinbreite").pack()
stone_width = Entry(top)
stone_width.pack()

label_bearing_joint = Label(top, text="Lagerfuge: 1,2 cm")
label_bearing_joint.pack()

label_butt_joint = Label(top, text="Stoßfuge: 0,8 cm")
label_butt_joint.pack()

Label(top, text="Mauerhöhe").pack()
wall_height = Entry(top)
wall_height.pack()

Label(top, text="Mauerlänge").pack()
wall_length = Entry(top)
wall_length.pack()

Label(top, text="Mauerbreite").pack()
wall_width = Entry(top)
wall_width.pack()


top.mainloop()