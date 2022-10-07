import random
import pygame
import math


pygame.init()

screen_width = 400
screen_height = 250

screen = pygame.display.set_mode([screen_width, screen_height])

color = ("Lightblue") 

screen.fill(color)

pygame.display.flip()

pygame.draw.circle(screen, "Red", (screen_width/2, screen_height/2) , 100) #screen_with/2
pygame.draw.line(screen, "Black", (screen_width/2, screen_height/2 +100), (screen_width/2, screen_height/2 - 100))
pygame.draw.line(screen, "Black",(screen_width/2 - 100,screen_height/2) , (screen_width/2 + 100,screen_height/2))

pygame.display.flip()
pygame.time.wait(500)

# part b
center_of_circle = (screen_width/2, screen_height/2)

for _ in  range(10):
 x1 = random.randrange(0,screen_width+1)  
 x2 = screen_width/2
 y1 = random.randrange(0,screen_height+1)
 y2 = screen_height/2
 
 distance_from_center = math.hypot(x1-x2, y1-y2) 
 is_in_circle = distance_from_center <= screen_width/2
 print(distance_from_center)

  
 if is_in_circle == True:
  pygame.draw.circle(screen, "Purple", (x1, y1) , 5)
  pygame.time.wait(1000)
  print(is_in_circle)
  pygame.display.flip()
   
 if is_in_circle == False:
  pygame.draw.circle(screen, "Green", (x1, y1) , 5)
  pygame.time.wait(1000)
  print(is_in_circle)
  pygame.display.flip()
  

pygame.time.wait(1000)

# part c
screen.fill(color)

pygame.display.flip()

pygame.draw.circle(screen, "Red", (screen_width/2, screen_height/2) , 100) 
pygame.draw.line(screen, "Black", (screen_width/2, screen_height/2 +100), (screen_width/2, screen_height/2 - 100))
pygame.draw.line(screen, "Black",(screen_width/2 - 100,screen_height/2) , (screen_width/2 + 100,screen_height/2))

pygame.display.flip()
pygame.time.wait(500)



# player_a = 
# player_b =

# player_a.color("Green")
# player_b.color("Purple")



# for _ in range(10):
  