import turtle


def draw_square():
    turtle.shape('turtle')

    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)

    turtle.exitonclick()


if __name__ == '__main__':
    draw_square()
