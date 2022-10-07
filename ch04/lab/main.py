import random
import pygame
import math


pygame.init()

screen_width = 250
screen_height = 250

screen = pygame.display.set_mode([screen_width, screen_height])

color = ("Lightblue") 

screen.fill(color)

pygame.display.flip()

pygame.draw.circle(screen, "Red", (screen_width/2, screen_height/2) , 125) #screen_with/2
pygame.draw.line(screen, "Black", (screen_width/2, screen_height/2 +125), (screen_width/2, screen_height/2 - 125))
pygame.draw.line(screen, "Black",(screen_width/2 - 125,screen_height/2) , (screen_width/2 + 125,screen_height/2))

pygame.display.flip()
pygame.time.wait(500)

# part b
center_of_circle = (screen_width/2, screen_height/2)

for _ in  range(10):
 x1 = random.randrange(0,screen_width+1)  
 x2 = 125
 y1 = random.randrange(0,screen_height+1)
 y2 = 125
 
 distance_from_center = math.hypot(abs(x1-x2), abs(y1-y2))
 is_in_circle = distance_from_center <= 125
 #print(distance_from_center)
 coords = (x1, y1)
  
 if is_in_circle == True:
  pygame.draw.circle(screen, "Purple", coords , 5)
  pygame.time.wait(1000)
 # print(is_in_circle)
  pygame.display.flip()
   
 elif is_in_circle == False:
  pygame.draw.circle(screen, "Green", coords , 5)
  pygame.time.wait(1000)
 # print(is_in_circle)
  pygame.display.flip()
  

pygame.time.wait(1000)

# part c
screen.fill(color)

#pygame.display.flip()


#while
#make a hitbox as well as the "buttons"
Hit_box1 = pygame.draw.rect(screen, "Green", (0, 0, 125, 250))
Hit_box2 = pygame.draw.rect(screen, "Purple", (125, 0 , 125, 250) )
pygame.display.flip()
pygame.time.wait(1000)
happy = ""
while True:
 
 for event in pygame.event.get():
  if event.type == pygame.MOUSEBUTTONDOWN:
   mouse_pos = pygame.mouse.get_pos()
  if event.button == Hit_box1:
   happy = ("You think that Green will win") 
  elif event.button == Hit_box2:
   happy = ("You think that Purple will win")
  print(happy)
pygame.display.flip()
pygame.time.wait(1000)








pygame.draw.circle(screen, "Red", (screen_width/2, screen_height/2) , 125) #screen_with/2
pygame.draw.line(screen, "Black", (screen_width/2, screen_height/2 +125), (screen_width/2, screen_height/2 - 125))
pygame.draw.line(screen, "Black",(screen_width/2 - 125,screen_height/2) , (screen_width/2 + 125,screen_height/2))

pygame.display.flip()
pygame.time.wait(500)

for _ in range(10):
 x1 = random.randrange(0,screen_width+1)  
 x2 = 125
 y1 = random.randrange(0,screen_height+1)
 y2 = 125
 
 distance_from_center = math.hypot(abs(x1-x2), abs(y1-y2))
 is_in_circle = distance_from_center <= 125
 #print(distance_from_center)
 coords = (x1, y1)



player_1 = 

  
 if is_in_circle == True:
  pygame.draw.circle(screen, "Green", coords , 5)
  pygame.time.wait(1000)
 # print(is_in_circle)
  pygame.display.flip()
   
 elif is_in_circle == False:
  pygame.draw.circle(screen, "DarkGreen", coords , 5)
  pygame.time.wait(1000)
 # print(is_in_circle)
  pygame.display.flip()
  

pygame.time.wait(1000)


player_2 = 

  
 if is_in_circle == True:
  pygame.draw.circle(screen, "Purple", coords , 5)
  pygame.time.wait(1000)
 # print(is_in_circle)
  pygame.display.flip()
   
 elif is_in_circle == False:
  pygame.draw.circle(screen, "DarkPurple", coords , 5)
  pygame.time.wait(1000)
 # print(is_in_circle)
  pygame.display.flip()
  

pygame.time.wait(1000)
# player_a = 
# player_b =

# player_a.color("Green")
# player_b.color("Purple")



# for _ in range(10):
  