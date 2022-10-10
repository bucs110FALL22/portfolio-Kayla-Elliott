def star_pyramid():
  print("Please enter a number:")
rows = int(input(":"))

for _ in range(1, rows + 1):
  print("*" * _)




def star_pyramidz():
  print("Please enter a number:")
rows = int(input(":"))

for _ in reversed(range(1, rows + 1)):
  print("*" * _)
