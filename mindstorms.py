import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("gray")

    draw_square()
    draw_circle()
    draw_triangle()

    
    window.exitonclick()

def draw_square():
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.shapesize(3,3,6)
    brad.color("dark green")
    brad.speed(2)
    for x in range(0,4):
        brad.forward(100)
        brad.right(90)

def draw_circle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

def draw_triangle():
    jorge = turtle.Turtle()
    jorge.shape("arrow")
    jorge.color("red")
    for y in range(0,3):
        jorge.forward(60)
        jorge.left(120)
 
    
draw_shapes()
