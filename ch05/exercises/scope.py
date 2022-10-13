numb1 = int(input("Enter your first number:"))
numb2 = int(input("Enter your second number:"))

multiplication_list = [numb1,numb2]


for _ in multiplication_list:
 result = numb1 * numb2

print(result, "is your result")




base = int(input("Enter your base number:"))
exponent = int(input("Enter your exponent number:"))


def expo(base, exponent):
  resu = 1
  for _ in range(exponent):
    resu = resu * exponent
print(resu, "is your result")