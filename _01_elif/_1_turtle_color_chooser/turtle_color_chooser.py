import random
import turtle
from tkinter import simpledialog


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


# ====================== DO NOT EDIT THE CODE ABOVE ===========================

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # TODO 1) Create a new Turtle
    ellie = turtle.Turtle()


    for i in range(6):
        colorChooser= simpledialog.askstring(title = '', prompt = 'What color pen would you like to draw with?')
        if colorChooser == 'red':
            ellie.pencolor('red')
        if colorChooser == 'orange':
            ellie.pencolor('orange')
        if colorChooser == 'yellow':
            ellie.pencolor('yellow')
        if colorChooser == 'green':
            ellie.pencolor('green')
        if colorChooser == 'blue':
            ellie.pencolor('blue')
        if colorChooser == 'purple':
            ellie.pencolor('purple')
        ellie.pensize(10)
        for i in range(4):
            ellie.forward(100)
            ellie.right(90)


    #      2) Make the turtle draw a shape (this will take more than one line
    #         of code)
    #      3) Set the pen width to 10
    #      4) Ask the user what color pen they would like to draw with
    #      5) Use an if/else statement to set the pen color that the user
    #         requested
    #      6) If the user doesn't enter anything, choose a random color
    #      7) Put a loop around your code so that you keep asking the user for
    #         more colors & drawing them

    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
