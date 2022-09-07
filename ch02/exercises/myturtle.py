import turtle

my_turtle = turtle.Turtle



num_sides = int(input("Number of sides of your shape?:"))
my_turtle.color("purple")
length = 50
angle = 360/ num_sides


for s in [angle]*num_sides:
  my_turtle.forward(length)
  my_turtle.right(s)  



my_turtle.color("red")
up()
left(70)


window.exitonclick()

