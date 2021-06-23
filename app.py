from tkinter import *
#from tkinter.ttk import *
import tkinter
import os

bg_c1 = "#1A1B1F"
bg_c2 = "#252525"
fg_c1 = "#81888C"
fg_c2 = "#F2F2F3"

bearing_joint_val = 1.2
butt_joint_val = 0.8

top = tkinter.Tk()
top.geometry("500x800")

#style = Style()
#style.configure("TEntry", fieldbackground=bg_c2)
#style.configure("Button", bg=bg_c2)

top.configure(bg=bg_c1)

warning_val = tkinter.StringVar(top)
wall_area_val = tkinter.DoubleVar(top)
stone_count_height_val = tkinter.DoubleVar(top)
stone_count_length_val = tkinter.DoubleVar(top)
stones_needed_val = tkinter.DoubleVar(top)
mortar_needed_bearing_joint = tkinter.DoubleVar(top)
mortar_needed_butt_joint = tkinter.DoubleVar(top)
mortar_needed_overall = tkinter.DoubleVar(top)


def calculate():
    if isValueMissing():
        warning_val.set("Fehler: Werte benötigt...")
    else:
        warning_val.set("")
        wall_area_val.set((int(wall_height.get()) * int(wall_length.get())) / 10000)
        stone_count_height_val.set(
            (int(wall_height.get()) + bearing_joint_val) / int(stone_height.get())
        )
        stone_count_length_val.set(
            int(wall_length.get()) / (int(stone_length.get()) + butt_joint_val)
        )
        stones_needed_val.set(
            stone_count_height_val.get() * stone_count_length_val.get()
        )
        mortar_needed_bearing_joint.set(
            (
                stone_count_height_val.get()
                * int(wall_length.get())
                * bearing_joint_val
                * int(stone_width.get())
            )
            / 1000000
        )
        mortar_needed_butt_joint.set(
            (
                int(stone_height.get())
                * int(stone_width.get())
                * butt_joint_val
                * stones_needed_val.get()
            )
            / 1000000
        )
        mortar_needed_overall.set(
            mortar_needed_bearing_joint.get() + mortar_needed_butt_joint.get()
        )


def isValueMissing():
    missing = (
        wall_height.index("end") == 0
        or wall_length.index("end") == 0
        or stone_height.index("end") == 0
        or stone_length.index("end") == 0
        or stone_width.index("end") == 0
    )
    if missing:
        return True
    try:
        int(wall_height.get())
        int(wall_length.get())
        int(stone_height.get())
        int(stone_length.get())
        int(stone_width.get())
    except ValueError:
        return True
    return False

frame = Frame(top, relief=RAISED, borderwidth=3, bg=bg_c1)
frame.pack(fill=BOTH, expand=True)

warning_label = Label(frame, textvariable=warning_val, bg=bg_c1, fg="coral").pack()

sub_frame1 = Frame(frame, bg=bg_c1)
sub_frame1.pack(fill=X)

Label(sub_frame1, text="Steinhöhe", bg=bg_c1, fg=fg_c1).pack(side=LEFT, padx=5)
stone_height = Entry(sub_frame1, bg=bg_c2, fg=fg_c2)
stone_height.pack(side=LEFT)

stone_length = Entry(sub_frame1, bg=bg_c2, fg=fg_c2)
stone_length.pack(side=RIGHT)
Label(sub_frame1, text="Steinlänge", bg=bg_c1, fg=fg_c1).pack(side=RIGHT, padx=5)

sub_frame2 = Frame(frame, bg=bg_c1)
sub_frame2.pack(fill=X)

Label(sub_frame2, text="Steinbreite", bg=bg_c1, fg=fg_c1).pack(side=LEFT, padx=5)
stone_width = Entry(sub_frame2, bg=bg_c2, fg=fg_c2)
stone_width.pack(side=LEFT)

sub_frame3 = Frame(frame, bg=bg_c1)
sub_frame3.pack(fill=X)

Label(sub_frame3, text="Lagerfuge in cm: ", bg=bg_c1, fg=fg_c1).pack(side=LEFT, padx=5)
Label(sub_frame3, text=bearing_joint_val, bg=bg_c1, fg=fg_c1).pack(side=LEFT, padx=5)

Label(sub_frame3, text="Stoßfuge in cm: ", bg=bg_c1, fg=fg_c1).pack(side=LEFT, padx=5)
Label(sub_frame3, text=butt_joint_val, bg=bg_c1, fg=fg_c1).pack(side=LEFT, padx=5)

sub_frame4 = Frame(frame, bg=bg_c1)
sub_frame4.pack(fill=X)

Label(sub_frame4, text="Mauerhöhe in cm", bg=bg_c1, fg=fg_c1).pack(side=LEFT, padx=5)
wall_height = Entry(sub_frame4, bg=bg_c2, fg=fg_c2)
wall_height.pack(side=LEFT)

wall_length = Entry(sub_frame4, bg=bg_c2, fg=fg_c2)
wall_length.pack(side=RIGHT)
Label(sub_frame4, text="Mauerlänge in cm", bg=bg_c1, fg=fg_c1).pack(side=RIGHT, padx=5)

sub_frame5 = Frame(frame, bg=bg_c1)
sub_frame5.pack(fill=X)

Label(sub_frame5, text="Mauerbreite in Steinen", bg=bg_c1, fg=fg_c1).pack(side=LEFT, padx=5)
wall_width = Entry(sub_frame5, bg=bg_c2, fg=fg_c2)
wall_width.pack(side=LEFT)

Label(top, text="Mauerfläche in m²: ", bg=bg_c1, fg=fg_c1).pack()
Label(top, textvariable=wall_area_val, bg=bg_c1, fg=fg_c1).pack()

Label(top, text="Steinanzahl Mauerhöhe: ", bg=bg_c1, fg=fg_c1).pack()
Label(top, textvariable=stone_count_height_val, bg=bg_c1, fg=fg_c1).pack()

Label(top, text="Steinanzahl Mauerlänge: ", bg=bg_c1, fg=fg_c1).pack()
Label(top, textvariable=stone_count_length_val, bg=bg_c1, fg=fg_c1).pack()

Label(top, text="Steinbedarf: ", bg=bg_c1, fg=fg_c1).pack()
Label(top, textvariable=stones_needed_val, bg=bg_c1, fg=fg_c1).pack()

Label(top, text="Mörtelbedarf lagerfuge in m³: ", bg=bg_c1, fg=fg_c1).pack()
Label(top, textvariable=mortar_needed_bearing_joint, bg=bg_c1, fg=fg_c1).pack()

Label(top, text="Mörtelbedarf Stoßfuge in m³: ", bg=bg_c1, fg=fg_c1).pack()
Label(top, textvariable=mortar_needed_butt_joint, bg=bg_c1, fg=fg_c1).pack()

Label(top, text="Mörtelbedarf gesamt in m³: ", bg=bg_c1, fg=fg_c1).pack()
Label(top, textvariable=mortar_needed_overall, bg=bg_c1, fg=fg_c1).pack()

Button(top, text="Berechnen", bg=bg_c2, fg=fg_c2, command=calculate).pack()


top.mainloop()
