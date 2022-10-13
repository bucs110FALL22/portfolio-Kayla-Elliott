#def star_pyramid():
  #print("Please enter a number:")
#rows = int(input(":"))

#for _ in range(1, rows + 1):
  #print("*" * _)




#def star_pyramidz():
  #print("Please enter a number:")
#rows = int(input(":"))

#for _ in reversed(range(1, rows + 1)):
  #print("*" * _)






def star_pyramid(rows):
 for _ in range(1, rows + 1):
  print("*" * _)




def star_pyramidz(rows):
 for _ in reversed(range(1, rows + 1)):
  print("*" * _)



rows = int(input("Please enter a number:"))


#print(rows, id(rows))


star_pyramid(rows)
star_pyramidz(rows)

#print(rows, id(rows))
