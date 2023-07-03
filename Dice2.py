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

turtle.color("red")
turtle.frame = 0
turtle.frames = ["Dice1.gif", "Dice2.gif", "Dice3.gif", "Dice4.gif", "Dice5.gif", "Dice6.gif"]
turtle.shape("Dice1.gif")


turtle.goto(0, 0)


def animate2(x,y):
    turtle.frame += 1
    if turtle.frame >= len(turtle.frames):
        turtle.frame = 0
    turtle.shape(turtle.frames[turtle.frame])

    # set Timer
    wn.ontimer(turtle.animate2, 500)


def animate(x,y):
    if turtle.frame == 0:
        turtle.shape("Dice2.gif")
        turtle.frame = 1
    elif turtle.frame == 1:
        turtle.shape("Dice3.gif")
        turtle.frame = 2
    elif turtle.frame == 2:
        turtle.shape("Dice4.gif")
        turtle.frame = 3
    elif turtle.frame == 3:
        turtle.shape("Dice5.gif")
        turtle.frame = 4
    elif turtle.frame == 4:
        turtle.shape("Dice6.gif")
        turtle.frame = 5
    elif turtle.frame == 5:
        turtle.shape("Dice1.gif")
        turtle.frame = 0


turtle.listen
turtle.onclick(animate2)


while True:
    wn.update()
    print("Dice App")


wn.mainloop()

# player2 = Player()
# player2.goto(350, 0)


# set keyboard bindings
# wn.listen
# wn.onkey(player2.animate(), "left")

# Player.animate()
# player2.animate()


