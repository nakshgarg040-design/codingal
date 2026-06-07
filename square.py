import turtle

turtle.Screen().bgcolor("blue")

sr = turtle.Screen()
sr.setup(400, 300)

turtle.title("welcome to Turtle Window")


board = turtle.Turtle()


for i in range(4):
    board.forward(100)
    board.left(90)
    i = i+1