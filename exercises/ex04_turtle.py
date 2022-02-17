"""Art project: A sky of hot air balloons.
I have used random functions to create variety in the sky during each iteration of the scene.
This is seen in the position, number, and color of the balloons, baskets, and clouds (although all clouds are white).
I have embedded the cloud() function within the clouds() function, and the clouds() into the background().
I have also combined basket() into balloon(), and balloon() into balloons()."""


__author__ = "730359525"

from turtle import Turtle, colormode, done
from random import randint


def cloud(pen: Turtle, x: float, y: float) -> None:
    """Drawing a cloud for the background""" 
    pen.up()
    pen.goto(x, y)
    pen.down()
    pen.seth(0)
    pen.speed(0)
    pen.color("white", "white")
    pen.begin_fill()
    pen.left(160)
    pen.forward(15)
    pen.right(100)
    pen.circle(17, 100)
    pen.right(60)
    pen.circle(15, 90)
    pen.right(130)
    pen.circle(22, 140)
    pen.right(60)
    pen.circle(15, 110)
    pen.right(105)
    pen.circle(5, 200)
    pen.right(200)
    pen.circle(15, 110)
    pen.right(90)
    pen.circle(7, 150)
    pen.right(150)
    pen.circle(15, 190)
    pen.right(163)
    pen.forward(40)
    pen.towards(x, y)
    pen.goto(x, y)
    pen.end_fill()
    pen.up()


def clouds(pen: Turtle, number_of_clouds: int) -> None:
    """Using while loops and random functions to create varied cloud cover."""
    while number_of_clouds != 0:
        cloud(pen, randint(-200, 200), randint(-200, 200))
        number_of_clouds -= 1


def background(pen: Turtle) -> None:
    """Creating a sky blue background."""
    pen.speed(0)
    pen.up()
    pen.goto(0, -1000)
    pen.down()
    colormode(255)
    pen.fillcolor(18, 199, 249)
    pen.begin_fill()
    pen.circle(1000)
    pen.end_fill()
    clouds(pen, randint(1, 10))
    pen.ht()


def balloon(pen: Turtle, x: float, y: float) -> None:
    """Drawing a hot air balloon for the foreground"""
    pen.speed(0)
    pen.up()
    pen.goto(x, y)
    pen.down()
    pen.seth(0)
    colormode(255)
    pen.fillcolor(randint(0, 255), randint(0, 255), randint(0, 255))
    pen.begin_fill()
    pen.left(45)
    pen.circle(50, 270)
    pen.right(180)
    pen.circle(100, -35)
    pen.right(190)
    pen.forward(30)
    pen.forward(-30)
    pen.right(40)
    pen.circle(19, -80)
    pen.left(115)
    pen.forward(30)
    pen.forward(-30)
    pen.circle(100, -35)
    pen.end_fill()
    basket(pen, x, y)


def basket(pen: Turtle, x: float, y: float) -> None:
    """Drawing the basket for the hot air ballon"""
    pen.up()
    pen.goto((x - 51), (y - 68))
    pen.down()
    pen.speed(0)
    colormode(255)
    pen.fillcolor(randint(0, 255), randint(0, 255), randint(0, 255))
    pen.begin_fill()
    pen.left(40)
    pen.forward(25)
    pen.left(90)
    pen.forward(38)
    pen.left(90)
    pen.forward(25)
    pen.left(90)
    pen.forward(38)
    pen.end_fill()
    pen.ht()


def balloons(pen: Turtle, number_of_balloons: int) -> None:
    """Using while loops and random functions to create varied balloons."""
    while number_of_balloons != 0:
        pen.speed(10)
        balloon(pen, randint(-250, 250), randint(-250, 250))
        number_of_balloons -= 1


def main() -> None:
    """The entrypoint of my scene."""
    bruce: Turtle = Turtle()
    lee: Turtle = Turtle()
    background(bruce)
    balloons(lee, randint(1, 9))
    done()

    
if __name__ == "__main__":
    main()