"""Background for EX04"""

from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
bob: Turtle = Turtle()

bob.ht() and leo.ht()

leo.up()
leo.goto(-150, -100)
leo.down()
colormode(255)
leo.color((54, 193, 145), (54, 104, 193))
bob.up()
bob.goto(-150, -100)
bob.down()

leo.st()
i: int = 0

while i < 3:
    leo.forward(300)
    leo.left(120)
    i += 1

leo.ht()

bob.speed(9)
bob.color("black")
i: int = 0
while i < 3:
    bob.forward(300)
    bob.left(120)
    i += 1
i: int = 0
side_length: float = 300

while i < 100:
    bob.forward(side_length)
    bob.left(121)
    side_length = side_length * 0.97
    i += 1

done()