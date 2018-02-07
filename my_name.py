import turtle


def draw_letters():
    window = turtle.Screen()
    window.bgcolor("gray")

    draw_as()
    draw_bs()
    
    window.exitonclick()

def draw_as():
    art = turtle.Turtle()
    art.shape("turtle")
    art.shapesize(2,2,4)
    art.color("orange")
    art.speed(2)
    art.forward(100)
    art.backward(50)
    art.left(90)
    art.forward(100)
    art.right(90)
    art.backward(100)

def draw_bs():
    art = turtle.Turtle()
    art.shape("turtle")
    art.shapesize(2,2,4)
    art.color("green")
    art.goto(40,20)
    art.speed(2)
    art.pensize(10)
    art.forward(100)
    art.backward(50)
    art.left(90)
    art.forward(100)
    art.right(90)
    art.backward(100)
    
    
#   for x in range(0,4):
#        brad.forward(100)
#        brad.right(90)


#def draw_circle():
#    angie = turtle.Turtle()
#    angie.shape("arrow")
#    angie.color("blue")
#    angie.circle(100)

#def draw_triangle():
#    jorge = turtle.Turtle()
#    jorge.shape("arrow")
#    jorge.color("red")
#    for y in range(0,3):
#        jorge.forward(60)
#        jorge.left(120)
 
    
draw_letters()
