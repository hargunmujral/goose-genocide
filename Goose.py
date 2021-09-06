# Goose Genocide!
# Inspiration taken from "Cookie Clicker" by DashNet
# Compatible with Windows, Linux and MacOSX
# by @hargunmujral (Github)

import turtle

window = turtle.Screen()
window.setup(600, 594)
window.title("Goose Genocide!")
window.bgpic("waterloo2.gif")

window.register_shape("goose.gif")
window.register_shape("shield.gif")
window.register_shape("tool.gif")
window.register_shape("warrior.gif")

goose = turtle.Turtle()
goose.shape("goose.gif")
goose.speed(0)
goose.goto(0, -120)

shield = turtle.Turtle()
shield.shape("shield.gif")
shield.speed(0)
shield.goto(223, 220)
shield.clear()

tool = turtle.Turtle()
tool.shape("tool.gif")
tool.speed(0)
tool.goto(223, 153)
tool.clear()

warrior = turtle.Turtle()
warrior.shape("warrior.gif")
warrior.speed(0)
warrior.goto(223, 86)
warrior.clear()

counter = 0

text = turtle.Turtle()
text.hideturtle()
text.color("black")
text.penup()
text.goto(0, 200)
text.write(f"Killed: {counter}", align="center", font=("Times New Roman", 30, "bold"))


def click(x, y):
    global counter
    counter += 1
    text.clear()
    text.write(f"Killed: {counter}", align="center", font=("Times New Roman", 30, "bold"))


def click2(x, y):
    global counter
    counter += 2
    text.clear()
    text.write(f"Killed: {counter}", align="center", font=("Times New Roman", 30, "bold"))



       
goose.onclick(click)

window.mainloop()


