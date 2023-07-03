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


class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.direction = 'stop'
        self.shape("Dice1.gif")
        self.color("red")
        self.frame = 0
        self.frames = ["Dice1.gif", "Dice2.gif", "Dice3.gif", "Dice4.gif", "Dice5.gif", "Dice6.gif"]

    def animate(self):
        self.frame += 1
        if self.frame >= len(self.frames):
            self.frame = 0
        self.shape(self.frames[self.frame])

        # set Timer
        wn.ontimer(self.animate, 500)


player = Player()
player.goto(-350, 0)

player2 = Player()
player2.goto(350, 0)

wn.listen
wn.onkey(player2.animate(), "left")

#set keyboard bindings


#player.animate()
#player2.animate()



#def player_animate1():
   # player.shape("Dice1.gif")
   # time.sleep(0.5)
   # player.shape("Dice2.gif")
   # time.sleep(0.5)

#def player_animate0():
    #if player.shape() == "Dice1.gif":
       # player.shape("Dice2.gif")
   # elif player.shape() == "Dice2.gif":
       # player.shape("Dice3.gif")
    #elif player.shape() == "Dice3.gif":
       # player.shape("Dice4.gif")
  #  elif player.shape() == "Dice4.gif":
       # player.shape("Dice5.gif")
   # elif player.shape() == "Dice5.gif":
      #  player.shape("Dice6.gif")
   # elif player.shape() == "Dice6.gif":
      #  player.shape("Dice1.gif")

#def player_animate2():
    #if player.frame == 0:
     #   player.shape("Dice2.gif")
     #   player.frame = 1
    #elif player.frame == 1:
      #  player.shape("Dice3.gif")
      #  player.frame = 2
   # elif player.frame == 2:
       # player.shape("Dice4.gif")
       # player.frame = 3
   # elif player.frame == 3:
      # player.shape("Dice5.gif")
      #  player.frame = 4
    #elif player.frame == 4:
       # player.shape("Dice6.gif")
       # player.frame = 5
   # elif player.frame == 5:
       # player.shape("Dice1.gif")
       # player.frame = 0

while True:
    wn.update()
    print("Dice App")

wn.mainloop()

