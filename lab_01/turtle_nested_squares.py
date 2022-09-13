import turtle


def draw_nested_squares():
    number_of_squares = 10
    side_length = 25
    offset_value = 10
    side_gain = offset_value * 2

    turtle.shape('turtle')

    for i in range(number_of_squares):
        draw_square(side_length)
        perform_offset(offset_value)
        side_length += side_gain

    turtle.exitonclick()


def perform_offset(offset_value: int):
    turtle.penup()
    turtle.goto(turtle.xcor() - offset_value, turtle.ycor() - offset_value)
    turtle.pendown()


def draw_square(side_length: int):
    number_of_sides = 4
    angle_of_rotation = 90

    for i in range(number_of_sides):
        turtle.forward(side_length)
        turtle.left(angle_of_rotation)


if __name__ == '__main__':
    draw_nested_squares()
