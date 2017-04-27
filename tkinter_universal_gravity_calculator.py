# Universal Gravity Calculator (30pts)
# In physics, the force of gravity between two objects
# can be calculated using the equation:
# F = G * (m1 * m2) / r**2
# F is the force of gravity in Newtons
# G is the universal gravity constant (6.67e-11)
# m1 is the mass of first object in kg
# m2 is the mass of the second object in kg
# r is the center to center distance between the objects in meters

# Make a tkinter app with the following attributes:
# - use an App class
# - Add a title.
# - Make a label and entry widget for m1, m2, and r
# - Make a "Calculate" button widget to trigger a lambda function
# - Add a calculate label widget to display the answer
# - Make exceptions for division by zero and type conversion errors.
# - When "Calculate" is pushed, the result is displayed.  Yay!
# - Add an exception for the possible entry of zero radius (ZeroDivisionError Exception)
# - Make your app unique by changing 3 or more DIFFERENT style attributes or kwargs for your app.  Perhaps consider: fonts, color, padding, widths, etc).  Put a comment in your code to tell me what you changed. If you change the font for all the widgets, that is ONE thing.  If you add padx to all your app widgets, that is ONE thing.  If you change the color of all your blocks, that is ONE thing.


#font, fontsize, background

import math
import random
from tkinter import *
from tkinter import font

class App():
    def __init__(self,master):

        #display that shows the result/what you have typed in
        #self.eqn_var = StringVar()
        #self.eqn_var.set("")

        my_font = font.Font(family = "Comic Sans MS", size = 10)


        self.m1 = DoubleVar()
        self.m1.set("")
        self.m2 = DoubleVar()
        self.m2.set("")
        self.r = DoubleVar()
        self.r.set("")
        self.answer = DoubleVar()
        self.answer.set("")


        self.title = Label(master, text="GRAVITY CALCULATOR", underline = 5, bg = "cyan")
        self.title.grid(row=1, column=1, columnspan =4, sticky='e' + 'w')

        self.result = Label(master, textvariable = self.answer)#, bg = "cyan")
        self.result.grid(row=5, column=2)

        self.m1_label = Label(master, text = "mass of the first object (kg)", font=my_font, bg = "cyan")
        self.m1_label.grid(row=2, column=1)
        self.entry1 = Entry(master, textvariable=self.m1, bg = "cyan")
        self.entry1.grid(row=3, column=1)

        self.m2_label = Label(master, text="mass of the second object (kg)", font=my_font, bg = "cyan")
        self.m2_label.grid(row=2, column=2)
        self.entry2 = Entry(master, textvariable=self.m2, bg = "cyan")
        self.entry2.grid(row=3, column=2)

        self.r_label = Label(master, text= "distance between the objects (m)", font = my_font, bg = "cyan")
        self.r_label.grid(row=2, column=3)
        self.entry3 = Entry(master, textvariable=self.r, bg = "cyan")
        self.entry3.grid(row=3, column=3)

        #number buttons

        self.calculate = Button(master, text="calculate", command=lambda: self.solving(), bg = "cyan")
        self.calculate.grid(row=5,column=1)

        self.cyan = Label(master, bg = "cyan")
        self.cyan.grid(row=6, column =1, columnspan = 4, sticky= "e" + "w")
        #self.cyan = Label(master, bg="cyan")
        #self.cyan.grid(row=5, column=2, columnspan=4, sticky="e" + "w")

    def solving(self):
        try:
            self.answer.set(((6.67 * (10 ** -11) * self.m1.get() * self.m2.get() / self.r.get() ** 2)))
        except ZeroDivisionError:
            self.answer.set("you can't divide by zero")





if __name__ == "__main__":
    root = Tk()
    my_app = App(root)
    root.mainloop()

