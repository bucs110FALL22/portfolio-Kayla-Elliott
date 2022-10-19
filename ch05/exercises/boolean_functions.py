


def percentage_to_letter(score=0):
    if score >= 90:
      letter = "A"
      return("A")
      print(letter)

    elif 80 <= score < 90:
      letter = "B"
      return("B")
      print(letter)

    elif 70 <= score < 80:
      letter = "C"
      return("C")
      print(letter)

    elif 60 <= score < 70:
      letter = "D"
      return("D")
      print(letter)

    elif score <= 60:
      letter = "F"
      return("F")
      print(letter)



def is_passing(letter=None):
  while True:
    if letter == "A" or letter == "B" or letter == "C":
      return(True)
    else:
      return(False)






score1 = int(input("Input your grade score with a number beween 0 and 100:"))




letter1 = percentage_to_letter(score1)

bsbs = is_passing(letter1)
print(letter1)

if bsbs == True:
  print("You are passing")
 
else:
   print("You are failing")
