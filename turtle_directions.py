from turtle import Turtle,Screen

tim = Turtle()
tim.shape("turtle")
screen = Screen()

def move_forward():
    tim.forward(10)
    tim.color("red")

def move_backwards():
    tim.back(10)
    tim.color("green")

def move_counterwise():
    tim.left(10)
    tim.color("blue")

def move_cloxkwise():
    tim.right(10)
    tim.color("orange")

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key ="w",fun= move_forward)
screen.onkey(key = "s",fun = move_backwards)
screen.onkey(key = "a",fun = move_counterwise)
screen.onkey(key = "d",fun = move_cloxkwise)
screen.onkey(key = "c",fun = clear )


screen.exitonclick()