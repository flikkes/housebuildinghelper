from tkinter import *
import tkinter
import os


bearing_joint_val = 1.2
butt_joint_val = 0.8

top = tkinter.Tk()
top.geometry("500x800")

wall_area_val = tkinter.DoubleVar(top)
stone_count_height_val = tkinter.DoubleVar(top)
stone_count_length_val = tkinter.DoubleVar(top)
stones_needed_val = tkinter.DoubleVar(top)
mortar_needed_bearing_joint = tkinter.DoubleVar(top)
mortar_needed_butt_joint = tkinter.DoubleVar(top)
mortar_needed_overall = tkinter.DoubleVar(top)


def calculate():
    wall_area_val.set((int(wall_height.get())*int(wall_length.get()))/10000)
    stone_count_height_val.set((int(wall_height.get())+bearing_joint_val)/int(stone_height.get()))
    stone_count_length_val.set(int(wall_length.get())/(int(stone_length.get())+butt_joint_val))
    stones_needed_val.set(stone_count_height_val.get()*stone_count_length_val.get())
    mortar_needed_bearing_joint.set((stone_count_height_val.get()*int(wall_length.get())*bearing_joint_val*int(stone_width.get()))/1000000)
    mortar_needed_butt_joint.set((int(stone_height.get())*int(stone_width.get())*butt_joint_val*stones_needed_val.get())/1000000)
    mortar_needed_overall.set(mortar_needed_bearing_joint.get()+mortar_needed_butt_joint.get())


Label(top, text="Steinhöhe").pack()
stone_height = Entry(top)
stone_height.pack()

Label(top, text="Steinlänge").pack()
stone_length = Entry(top)
stone_length.pack()

Label(top, text="Steinbreite").pack()
stone_width = Entry(top)
stone_width.pack()

Label(top, text="Lagerfuge in cm: ").pack()
Label(top, text=bearing_joint_val).pack()

Label(top, text="Stoßfuge in cm: ").pack()
Label(top, text=butt_joint_val).pack()

Label(top, text="Mauerhöhe in cm").pack()
wall_height = Entry(top)
wall_height.pack()

Label(top, text="Mauerlänge in cm").pack()
wall_length = Entry(top)
wall_length.pack()

Label(top, text="Mauerbreite in Steinen").pack()
wall_width = Entry(top)
wall_width.pack()

Label(top, text="Mauerfläche in m²: ").pack()
Label(top, textvariable=wall_area_val).pack()

Label(top, text="Steinanzahl Mauerhöhe: ").pack()
Label(top, textvariable=stone_count_height_val).pack()

Label(top, text="Steinanzahl Mauerlänge: ").pack()
Label(top, textvariable=stone_count_length_val).pack()

Label(top, text="Steinbedarf: ").pack()
Label(top, textvariable=stones_needed_val).pack()

Label(top, text="Mörtelbedarf lagerfuge in m³: ").pack()
Label(top, textvariable=mortar_needed_bearing_joint).pack()

Label(top, text="Mörtelbedarf Stoßfuge in m³: ").pack()
Label(top, textvariable=mortar_needed_butt_joint).pack()

Label(top, text="Mörtelbedarf gesamt in m³: ").pack()
Label(top, textvariable=mortar_needed_overall).pack()

Button(top, text= "Berechnen", command=calculate).pack()


top.mainloop()
