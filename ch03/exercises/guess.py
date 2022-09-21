import random

answer = random.randint(1,10)

guess = (int(input("Guess a number between 1 and 10 in 3 tries or less!:")))
correct = False

for _ in range(2):  #range(2) because range(3)  gave four tries
  if answer == guess:
    print("Your guess was correct!") 
    correct = True
    break
    
  elif guess > answer:
    guess = (int(input("Your guess was too high:")))
  elif guess < answer:
    guess = (int(input("Your guess was too low:")))

if not correct: 
  print(answer)
 

  
   

#what about after the loop, want to know what the number was
#how to get out of the dotten lines after doe with all of the if else statments 

#  x!=y is for those that are not equal
# >= and <= also exist