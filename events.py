from turtle import *

class MyTurtle(Turtle):
    """My own version of turtle"""
    def __init__(self,*args,**kwargs):
        super(MyTurtle,self).__init__(*args,**kwargs)
        print("Time for my GTX turtle!")

    def glow(self,x,y):
        self.fillcolor("red")
    def unglow(self,x,y):
        self.fillcolor("")

    def up(self):
        self.setheading(90)
        self.forward(100)

    def down(self):
        self.setheading(270)
        self.forward(100)

    def left(self):
        self.setheading(180)
        self.forward(100)

    def right(self):
        self.setheading(0)
        self.forward(100)

    def orig(self):
        self.pu()
        self.goto(0,0)
        self.pd()

if __name__ == '__main__':
    screen = Screen()

    player1 = MyTurtle()
    player1.fillcolor('red')
    player2 = MyTurtle()
    player2.fillcolor('blue')

    screen.listen()

    screen.onkey(player1.up, 'Up')
    screen.onkey(player1.down, 'Down')
    screen.onkey(player1.left, 'Left')
    screen.onkey(player1.right, 'Right')
    screen.onkey(player1.orig, 'space')

    screen.onkey(player2.up, 'w')
    screen.onkey(player2.down, 's')
    screen.onkey(player2.left, 'a')
    screen.onkey(player2.right, 'd')
    screen.onkey(player2.orig,'q')

    screen.exitonclick()
