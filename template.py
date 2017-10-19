from turtle import *


class eTurtle(Turtle):
    """My own version of turtle"""
    def __init__(self,*args,**kwargs):
        super(eTurtle,self).__init__(*args,**kwargs)
        print("Time for my GTX turtle!")

    def square(self,size):
        for i in range(4):
            self.fd(size)
            self.right(90)

    def colorSquare(self,size,color):
        self.color("black","red")
        self.begin_fill()
        self.square(size)
        self.end_fill()


if __name__ == '__main__':
    screen = Screen()

    bob = eTurtle()
    bob.square(100)

    colorbob = eTurtle()
    colorbob.pu()
    colorbob.goto(100,100)
    colorbob.pd()
    print(colorbob.pos())
    colorbob.colorSquare(100,'red')

    screen.exitonclick()
