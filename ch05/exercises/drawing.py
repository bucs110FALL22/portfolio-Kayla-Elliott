import turtle



def drawEqShape(tur, num_sides, length):
 angle = 360/ num_sides
 for _ in [angle]*num_sides:
   tur.forward(length)
   tur.right(_)  

turguy = turtle.Turtle()
turguy.color("Green")
turguy.shape("turtle")

num_sides = int(input("Number of sides of your shape?:"))
length =  int(input("How long do you want the sides to be:"))
tur_move = [turguy, num_sides, length]
window = turtle.Screen() # 2.  Create a screen
window.bgcolor("Lightblue")
drawEqShape(*tur_move)
drawEqShape(turguy, num_sides, length)





window.exitonclick()