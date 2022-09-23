import turtle #1. import modules
import random
import time 
import pygame
import math

#Part A


window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
time.sleep(3)
## 5. Your PART A code goes here

michelangelo.forward(random.randrange(1,101))
time.sleep(2)
leonardo.forward(random.randrange(1,101))
time.sleep(2)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
time.sleep(2)

for _ in range(10):
  michelangelo.forward(random.randrange(1,11))
  time.sleep(2)
  leonardo.forward(random.randrange(1,11))
  time.sleep(2)

michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

window.exitonclick()
# PART B - complete part B here
pygame.init()
window = pygame.display.set_mode()

coords = []
numb_sides  =  [3,4,6,9,360]
side_length =  50
offset = 100
window.fill(pygame.Color("gray96"))

for i in range(5):
  for _ in range(numb_sides[i]):  
   angle = (2.0 * math.pi * (_)) / numb_sides[i]
   x = side_length * math.cos(angle) + offset
   y = side_length * math.sin(angle) + offset
   coords.append([x,y])
  pygame.draw.polygon(window, "hotpink", coords) 
  pygame.display.flip()
  coords.clear()
  pygame.time.wait(1000)
  window.fill(pygame.Color("gray96"))



#window.exitonclick()