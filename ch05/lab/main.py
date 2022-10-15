import random
import pygame


#n = int(input("Please enter a number:"))

#since n can not be used, but we need then to repetedly go through the loops to gain each 


# since n cannot be used we have to start at 2 and go up to the upper mitit +1 but we can t use start because taht doesnt work, so is it what we need a new variable but if so why wont start work, showld I just put what start is but then what whould I use start for? 

upper_limit = 20 #20
iters = {}
#n = int(input("Please enter a number:"))
#SCALE = 5

  
  
#for n in range(start, stop):
#def loops(n=0):

  #n = value
  #n = 0 + sb
for _ in range(2, upper_limit + 1):  
  n = _
  #print(_)
  count = 0
  while (n != 1):  
    if (n % 2) == 0:
      n = n//2
    
    else:
      n = 3*n + 1
    count += 1
    #print(count)
    
    iters[_] = count
    
print(iters)







#sequence(n)

  #count = sequence(_)

# not working in correct order, it is using the upper_limit for some ungodly reason

#for value in range(2, upper_limit + 1):
  #count = 0
  #n = value
  #n = 0 + sb
  #while (n != 1):
       
    #if (n % 2) == 0:
      #n = n//2
      #count += 1
     
    #else:
      #n = 3*n + 1
      #count = count + 1
    

   #if (n == 1):
#iters[n] = count
#iters[value * SCALE] = count * SCALE
     
   #iters.update({couny :count})

    

#print(iters)


# make a variable for 



  