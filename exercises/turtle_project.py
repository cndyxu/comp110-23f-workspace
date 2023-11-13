"""Using Turtle to create a very basic Christmas morning by using the setheading() method to turn the triangle function to the right orientation, calling the rectangle function as a tree trunk, using a while loop to replicate three of the triangles to create a Christmas tree, and ending the main function by calling the square function as a present!"""

# __author__ = "730479883"

from turtle import Turtle, colormode, done
colormode(225)
t1 = Turtle()


def square(turtle: Turtle, x: int, y: int, length: int = 100) -> None:
    """Draws a sqaure of specified length, size, and place."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(0)

    turtle.color("black", "red")
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(length)
        turtle.right(90)
    
    turtle.end_fill()


def triangle(turtle: Turtle, x: int, y: int) -> None:
    """Draws one green equalateral triangles of specified size and place."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(240)

    turtle.color("green", "green")
    turtle.begin_fill()

    for _ in range(3):
        turtle.forward(200)
        turtle.left(120)

    turtle.end_fill()


def rectangle(turtle: Turtle, x: int, y: int, length: int = 10, height: int = 100) -> None:
    """Draws one brown rectangle of specified length, height, size, and place."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(0)

    turtle.color("brown", "brown")
    turtle.begin_fill()

    for _ in range(4):
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(height)
        turtle. right(90)
    
    turtle.end_fill()

        
def main(turtle: Turtle, x: int = 0, y: int = 200) -> None:
    """Creating a Christmas tree by calling the previous functions defined"""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    i: int = 0

    rectangle(t1, 0, -100)

    while (i < 3):
        triangle(t1, x, y)
        y -= 75
        i += 1
    
    square(t1, 60, -100)
    return

main(t1, 0, 200)

done()
