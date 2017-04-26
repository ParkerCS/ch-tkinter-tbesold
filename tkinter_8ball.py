# MAGIC 8-BALL (25pts)
# Create a tkinter app which acts as a "Magic 8-ball" fortune teller
# The user asks a yes/no question that they want an answer to.
# Then the user clicks a button, and your program displays
# the "magic" random answer to their question.
# Your program will have the following properties:
# - Use an App class to create the tkinter app
# - Add a proper title (appears in the window tab)
# - Add a Label widget at the top to give the user instructions/intro.
# - Add an Entry widget so the user can enter their question.
# - Add a Button widget which will trigger the answer.
# - Add a Label widget to display the answer (set to a initial value of "Your Fortune Here" or "--" or similar)
# - Get your random answer message from a list of at least 10 possible strings. (e.g. ["Yes", "No", "Most Likely", "Definitely", etc...])
# - Add THREE or more other style modifications to make your app unique (font family, font size, color, padding, image, borders, justification, whatever you can find in tkinter library etc.)  Make a comment at the top or bottom of your code to tell me your 3 things you did. (Just to help me out in checking your assignment)



import math
import random
from tkinter import *

# color of text, background color, and padding


class App():
    def __init__(self, master):   #the master is sending the root stuff in
        answers = ["yes", "no", "possibly", "it depends who you ask", "ask again later", "almost certainly", "maybe", "there's a chance", "who knows?", "for sure"]
        #randum = random.randrange(9)
        #answer = answers[randum]

        #my variables
        self.mystring = StringVar()
        self.mystring.set("")

        #label widget
        self.title = Label(master, text="8 BALL", bg="black", fg= "cyan", width =22)
        self.title.grid(row = 1, column = 1, columnspan =3, sticky='e' + 'w')

        self.answ = Label(master, textvariable = self.mystring, pady = 4, fg = "black", bg = "cyan")
        self.answ.grid(row =4, column =1, stick = "e" + "w", columnspan = 3)

        self.txt = Label(master, text = "Enter a yes or no question below")
        self.txt.grid(row = 2, column =1, columnspan =3, sticky='e' + 'w')

        #add a button
        self.button = Button(master, text = "click here", command=lambda:self.mystring.set(answers[random.randrange(len(answers))]))
        self.button.grid(row =3, column = 3)

        #add entry widget
        self.enter = Entry(master)
        self.enter.grid (row = 3, column = 1)


if __name__ == "__main__":
    root = Tk()
    my_app = App(root)
    root.mainloop()     #this will create a window
