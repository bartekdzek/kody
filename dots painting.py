# import colorgram
import turtle, random
# colors = colorgram.extract("image.jpg", 30)
jacob = turtle.Turtle()
jacob.hideturtle()
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# clrs = rgb_colors

clrs = [(233, 233, 232), (231, 233, 237), (235, 231, 233), (224, 233, 227), (207, 160, 82), (54, 88, 130), (145, 91, 40), (140, 26, 48), (222, 206, 108), (132, 177, 203), (158, 46, 83), (45, 55, 104), (169, 160, 39), (129, 189, 143), (83, 20, 44), (37, 43, 67), (186, 94, 107), (186, 140, 170), (85, 120, 180), (59, 39, 31), (88, 157, 92), (78, 153, 165), (195, 79, 72), (161, 201, 219), (45, 74, 77), (79, 74, 44), (57, 126, 122), (218, 175, 187), (168, 206, 169), (220, 182, 168)]
turtle.colormode(255)
jacob.speed("fastest")

for _ in range(10):
    for _ in range(10):
        clr = random.choice(clrs)
        jacob.pencolor(clr)
        jacob.pendown()
        jacob.dot(10)
        jacob.penup()
        jacob.forward(30)
    jacob.left(180)
    jacob.forward(300)
    jacob.right(90)
    jacob.forward(30)
    jacob.right(90)


screen = turtle.Screen()
screen.exitonclick()
