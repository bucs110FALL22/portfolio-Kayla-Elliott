# was i suposed to use a command for the exponent and multplication? having problems with the squares

def multy(numb1 = 0, numb2 = 0):
 #result = numb1 * numb2
 #print(result, "is your result")
  result = 0 
  for _ in range(numb1):
    result += numb2
  return(result)
#add numb1 to numb1 numb2 times

numb1 = int(input("Enter your first number:"))
numb2 = int(input("Enter your second number:"))

rere = multy(numb1, numb2)
print(rere, "is your result")


def expo(base = 0, exponent = 0):
  #result = base ** exponent
  #print(result, "is your result")
  result = 1
  for _ in range(exponent):
    result *= base
  return(result)

base = int(input("Enter your base number:"))
exponent = int(input("Enter your exponent number:"))


bolo = expo(base, exponent)
print(bolo, "is your result")



def square(single = 0):
  return (expo(single, 2))
  



single = int(input("Enter number you want squared:"))

scep = square(single)
print(scep)

#def expo(base, exponent):
  #resu = 1
 # for _ in range(exponent):
  #  resu = resu * exponent
#print(resu, "is your result")