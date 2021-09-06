# Goose Clicker Action Packed I
# Inspiration taken from "Cookie Clicker" by DashNet
# Compatible with Windows, Linux and MacOSX
# by @hargunmujral (Github)

import turtle

window = turtle.Screen()
window.setup(600, 594)
window.title("Goose Clicker!")
window.bgpic("waterloo2.gif")
window.register_shape("goose.gif")

goose = turtle.Turtle()
goose.shape("goose.gif")
goose.speed(0)
goose.goto(0, -120)

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


def grandma(x, y):
    global counter
    while counter >= 100:
        

goose.onclick(click)

window.mainloop()


