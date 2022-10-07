import turtle
import random


window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')
# how to create 



turguy = turtle.Turtle()
turguy.color('Blue')
turguy.shape('turtle')

turguy.down()


turguy.goto(0,0)

while True:  #so here is where i put the statment to keep the turtle in the screen?
  coin = random.randint(1,2)
  if coin == 1:
    heads = turguy.left(90) 
    turguy.forward(50)

  elif coin == 2:
   tails = turguy.right(90) 
   turguy.forward(50)






