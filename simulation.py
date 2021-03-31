import turtle as davison
import random

class buffon():
    ##initiating variables for speed, number of needles and grid
    def __init__(self, needles):
        davison.setworldcoordinates(-30, -30, 130, 130)
        davison.speed(0)
        self.needles = needles
        self.intersect = 0
        self.draw_grid()
        print((2 * self.needles) / self.intersect) ##formula is 2l/xp

    ##drawing out the grid
    def draw_grid(self):
        for i in range(0, 120, 20):
            davison.color("black")
            davison.penup()
            davison.setpos(0, i)
            davison.pendown()
            davison.forward(100)
        self.drop_needles()

    ##placing out the needles
    def drop_needles(self):
        davison.color("red")
        for i in range(self.needles):
            davison.penup()
            davison.goto(random.randrange(10, 90), random.randrange(0,100))
            y1 = davison.ycor()
            davison.seth(360 * random.random())
            davison.pendown()
            davison.forward(20)
            y2 = davison.ycor()

            for j in range(0, 120, 20):
                if y1 > y2:
                    if j < y1 and j > y2:
                        self.intersect += 1
                        print(f"Intersection! {y1,y2}")
                else:
                    if i > y1 and i < y2:
                        self.intersect += 1
                        print(f"Intersection! {y1, y2}")

buffon(100)
