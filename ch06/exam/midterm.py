import turtle

my_turtle = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("lightblue")
#how about instead we just deffined the shapes itself and how to make them
turguy = turtle.Turtle()
turguy.home()

rect_side = 4
rect_length1 = 25
rect_length2 = 50
cir_side = 360
tri_side = 3
tri_length = 25
cir_length = 5

angle1 = 360/ rect_side
angle2 = 360/ tri_side
angle3 = 360/ cir_side
angle4 = 45
angle5 = 60
angle6 = 120


rumb_large = 25
rumb_side = 12.5
rumb_small = 17.5

fotytri_t = 10
fotytri_g = 14.14




def Rect(turguy, rect_length1, rect_length2, angle1):
  turguy.fillcolor("lightgrey")
  #turguy.left()
  turguy.forward(rect_length1)
  turguy.left(angle1) 
  turguy.forward(rect_length2)
  turguy.left(angle1) 
  turguy.forward(rect_length1)
  turguy.left(angle1) 
  turguy.forward(rect_length2)
  
  #turguy.fillcolor("lightgrey")
  turguy.begin_fill()
  turguy.end_fill()




def Tri(turguy, tri_length, angle2):
  turguy.fillcolor("red")
  #turguy.left()  #will start in the same place as the rectangle for convenence
  turguy.forward(tri_length)
  turguy.right(angle2)
  turguy.forward(tri_length)
  turguy.right(angle2)
  turguy.forward(tri_length)
  turguy.right(angle2)
  #turguy.fillcolor("red")
  turguy.begin_fill()
  turguy.end_fill()



def Lef_rig(fotytri_t, fotytri_g, angle4):
  turguy.fillcolor("red")
  #will start 20 down from the top of the rectangle
  # :3
  #turguy.left() #how much it takes to turn to the left
  turguy.forward(fotytri_t) #number appropreate, make it cariable so can be reused
  turguy.right(angle4)
  turguy.forward(fotytri_g)
  turguy.right(angle4)
  turguy.forward(fotytri_t)
  #turguy.fillcolor("red")
  turguy.begin_fill()
  turguy.end_fill()



def Rig_rig(fotytri_t, fotytri_g, angle4):
  turguy.fillcolor("red")
  #turguy.right(180) #how much it takes to turn to the left
  turguy.forward(fotytri_t) #number appropreate, make it cariable so can be reused
  turguy.left(angle4)
  turguy.forward(fotytri_g)
  turguy.left(angle4)
  turguy.forward(fotytri_t)
  #turguy.fillcolor("red")
  turguy.begin_fill()
  turguy.end_fill()





def Rumb(rumb_large, rumb_side, rumb_small, angle6):
  turguy.fillcolor("grey")
  #will start at the bottom right of the rectangel
  #turguy.left(180)
  turguy.forward(rumb_large)
  turguy.left(angle5)
  turguy.forward(rumb_side)
  turguy.left(angle6)
  turguy.forward(rumb_small)
  turguy.left(angle6)
  turguy.forward(rumb_side)
  turguy.begin_fill()
  turguy.end_fill()
  
def Cir(cir_length, angle3):
  turguy.fillcolor("lightblue")
  #will start in the center of teh rectangel
  turguy.forward(cir_length)
  turguy.right(angle3)
  turguy.begin_fill()
  turguy.end_fill()
  

#have num sides and coords have a list so that if we have an iff statment with a range they could pull from both of them to get the andswerss??

#coords = turguy.position() [(), (),(),()]


def Drawship(turguy, rect_side, rect_length1, rect_length2 cir_side, cir_length, tri_side, tri_length, angle1, angle2, angle3, angle4, angle6, rumb_large, rumb_small, rumb_side,fotytri_t, fotytri_g):      
  
  turguy.goto(50,50)
  Rect(turguy, rect_length1, rect_length2, angle1)
  turguy.goto(50,50)
  Tri(turguy, tri_length, angle2)
  turguy.goto(25,70)
  Lef_rig(fotytri_t, fotytri_g, angle4)
  turguy.goto(50,70)
  Rig_rig(fotytri_t, fotytri_g, angle4)
  turguy.goto(50,100)
  Rumb(rumb_large, rumb_side, rumb_small, angle6)
  turguy.goto(37.5,75)
  Cir(ir_length, angle3)

 

Drawship(turguy, rect_side, rect_length1, rect_length2, cir_side, cir_length, tri_side, tri_length, angle1, angle2, angle3, rumb_large, rumb_small, rumb_side,fotytri_t, fotytri_g)



#yes = ['yes', 'y']
#no = ['no', 'n']




#space =  Drawship(turguy, screen, rect_side, rect_length, cir_side, cir_length, tri_side, tri_length, angle1, angle2, angle3, rumb_large, rumb_small, rumb_side,fotytri_t, fotytri_g)


#while True:
    #space_anima = int(input("Do you want to see a spaceship? (Y/N)"))
   # if space_anima.lower() in yes:
     #   Drawship(turguy, screen, rect_side, rect_length, cir_side, cir_length, tri_side, tri_length, angle1, angle2, angle3, rumb_large, rumb_small, rumb_side,fotytri_t, fotytri_g)
       # break
   # elif space_anima.lower() in no:   #i think we need something a bit more here
       # print("Are you sure")
       # break
  #  else:
      #  print(">|:( plz print either yes/y for yes or no/n for no:")
    #    continue

screen.exitonclick()