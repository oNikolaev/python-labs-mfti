import turtle


def draw_circle():
    number_of_sides = 100
    angle_of_rotation = 360 / number_of_sides
    side_length = 10

    turtle.shape('turtle')

    for i in range(number_of_sides):
        turtle.forward(side_length)
        turtle.left(angle_of_rotation)

    turtle.exitonclick()


if __name__ == '__main__':
    draw_circle()
