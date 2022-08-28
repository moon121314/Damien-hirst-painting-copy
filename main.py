import colorgram
import turtle as turtle_module
import random

rgb_colours =[]
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_colors=(r,g,b)
    rgb_colours.append(new_colors)

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
color_list=[(252, 250, 235), (241, 252, 245), (253, 245, 249), (232, 243, 249), (238, 231, 79), (180, 16, 43), (219, 64, 99), (109, 179, 204), (185, 74, 38), (25, 122, 166), (186, 42, 67), (207, 152, 102), (22, 136, 85), (188, 176, 23), (20, 31, 68), (216, 130, 154), (70, 170, 100), (19, 166, 208), (232, 230, 6), (217, 78, 55), (38, 46, 112), (127, 184, 138), (8, 51, 33), (235, 165, 182), (149, 210, 220), (163, 24, 20), (10, 98, 55), (156, 213, 189), (237, 171, 163), (87, 21, 61)]
#print(rgb_colours)
#print(colors)
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dot = 100
for i in range(1,number_of_dot+1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)
    if i % 10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



