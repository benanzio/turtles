import turtle

def draw_square(some_turtle):
    for i in range (1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("pink")
    #Create the turtle - draw a square
    pedro = turtle.Turtle()
    pedro.shape("turtle")
    pedro.color("black")
    pedro.speed(10)
    for i in range (1,37):
        draw_square(pedro)
        pedro.right(10)

draw_art()

