import turtle
turtle.Screen().bgcolor("black")

sc=turtle.Screen()
sc.setup(500,500)

turtle.title("welcome to my create a square")

board=turtle.Turtle()

board.fillcolor("white")
board.begin_fill()
board.forward(100)
board.left(90)

board.forward(100)
board.left(90)

board.forward(100)
board.left(90)

board.forward(100)
board.left(90)
board.end_fill()


turtle.done()