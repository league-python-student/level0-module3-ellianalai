def setup():
    # Set the size of your sketch
    size (500,500)
    
    
    
    pass
    
def draw():
    # Starting with the largest ellipse, use a for loop to draw a bullseye with ellipses
    for i in range(9):
        fill('')
        ellipse(250,250, 400 - (i*50), 400 - (i*50))
    # Use an if statement and modulo to alternate the color of your rings
    
    pass
    
    
    
    
    
