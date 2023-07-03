import turtle
import time

wn = turtle.Screen()
wn.title("Dice App")
wn.bgcolor("black")

# Registered shapes
wn.register_shape("Dice1.gif")
wn.register_shape("Dice2.gif")
wn.register_shape("Dice3.gif")
wn.register_shape("Dice4.gif")
wn.register_shape("Dice5.gif")
wn.register_shape("Dice6.gif")

turtle.goto(0, 0)
turtle.frame = 0
turtle.frames = ["Dice1.gif", "Dice2.gif", "Dice3.gif", "Dice4.gif", "Dice5.gif", "Dice6.gif"]
turtle.shape(turtle.frames[turtle.frame])


def animate2(x, y):
    turtle.frame += 1
    if turtle.frame >= len(turtle.frames):
        turtle.frame = 0
    turtle.shape(turtle.frames[turtle.frame])

    wn.ontimer(animate2, 500)


def animate(x, y):
    turtle.clear()
    turtle.shape((turtle.frames[turtle.frame]))
    turtle.penup()
    turtle.setpos(0, 0)
    turtle.pendown()


turtle.listen()
turtle.onclick(animate)

while True:
    wn.update()
    print("Dice App")

wn.mainloop()