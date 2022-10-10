import turtle
import random


window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')
# how to create 
turguy = turtle.Turtle()
turguy.color('Blue')
turguy.shape('turtle')


window_width = 250
window_height = 250


distance = 10
angle = 90
is_on_screen = True

colors = ["Red","Green","Purple"]

turguy.goto(0,0)

while is_on_screen:  #so here is where i put the statment to keep the turtle in the screen?
  coin = random.randint(0,1)
  if coin == 0:
   turguy.left(angle) 
   turguy.forward(distance)

  else:
   turguy.right(angle) 
   turguy.forward(distance)


   turtX = turguy.xcor()
   turtY = turguy.ycor()

   x_range = window.window_width()/2
   y_range = window.window_height()/2 


   turguy.color(colors[0])


   colors.append(colors.pop(0))
   if abs(turtX) > x_range or abs(turtY) > y_range:
     is_in_screen = False 

     window.bgcolor("Yellow")



   if turtX > window_width:
     turguy.goto(0,0)

   if turtY > window_height:
     turguy.goto(0,0)
     



    
window.exitonclick()
    
    





