import turtle

if __name__ == '__main__':
    ellie = turtle.Turtle()
    ellie.shape('turtle')
    ellie.color('yellow', 'green')
    ellie.speed(100)
    ellie.penup()

    # TODO 1) Set the X position of the turtle so that it starts on the left.
    ellie.goto(-200,100)
    ellie.pendown()
    # TODO 2) Make the turtle draw a star shape. Hint: angle=144.

    # Draw 5 stars
    for i in range (8):

        # Draw 1 star
        for k in range(5):
            ellie.forward(30)
            ellie.right(144)

        ellie.penup()
        ellie.goto(-150 + (i*50),100)
        ellie.pendown()

    # TODO 3) Set the length of each line in the star to 30

    # TODO: CHALLENGE
    #       Make the turtle draw a line of stars like the image in
    #       this folder.
    #       Hint: The distance between stars is 50.

# ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
