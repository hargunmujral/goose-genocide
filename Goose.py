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
boost1 = False
boost2 = False
boost3 = False

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

def null(x, y):
    text.clear()
    text.write(f"Killed: {counter}", align="center", font=("Times New Roman", 30, "bold"))

def click1(x, y):
    global counter
    counter += 5
    text.clear()
    text.write(f"Killed: {counter}", align="center", font=("Times New Roman", 30, "bold"))

def click2(x, y):
    global counter
    counter += 20
    text.clear()
    text.write(f"Killed: {counter}", align="center", font=("Times New Roman", 30, "bold"))

def click3(x, y):
    global counter
    counter += 50
    text.clear()
    text.write(f"Killed: {counter}", align="center", font=("Times New Roman", 30, "bold"))


def power1(x, y):
    global counter
    global boost1
    counter -= 100
    boost1 = True
    text.clear()
    text.write(f"Killed: {counter}", align="center", font=("Times New Roman", 30, "bold"))      

def power2(x, y):
    global counter
    global boost2
    counter -= 500
    boost2 = True
    text.clear()
    text.write(f"Killed: {counter}", align="center", font=("Times New Roman", 30, "bold"))      

def power3(x, y):
    global counter
    global boost3
    counter -= 2000
    boost3 = True
    text.clear()
    text.write(f"Killed: {counter}", align="center", font=("Times New Roman", 30, "bold"))      


while boost1 == False and boost2 == False and boost3 == False:
    if counter < 100:
        goose.onclick(click)
    elif counter >= 100 and counter < 500:
        shield.onclick(power1)
    
        

while boost1 == True and boost2 == False and boost3 == False:
    goose.onclick(click1)
    shield.onclick(null)
    if  counter >= 500 and counter < 2000:
        tool.onclick(power2)

while boost1 == True and boost2 == True and boost3 == False:
    goose.onclick(click2)
    tool.onclick(null)
    if counter >= 2000:
        warrior.onclick(power3)

while boost1 == True and boost2 == True and boost3 == True:
    goose.onclick(click3)
    warrior.onclick(null)

window.mainloop()


