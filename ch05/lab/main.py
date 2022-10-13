import turtle


n = int(input("Please enter a number:"))
print(n)
while (n != 1):
 if (n % 2) == 0:
  n = n/2
  print(n)
 else:
  n = 3*n + 1
  print(n)





count = 0 
n = int(input("Please enter a number:"))
print(n)
while (n != 1):
   if (n % 2) == 0:
    n = n/2
    count += 1
    print(n)
   else:
    n = 3*n + 1
    count += 1
    print(n)

print(count)




upper_limit = 20
iters = {}
count = 0 
n = int(input("Please enter a number:"))
print(n)
while (n != 1):
   if (n % 2) == 0:
    n = n/2
    count += 1
    print(n)
   else:
    n = 3*n + 1
    count += 1
    print(n)

print(count)


start = (2, upper_limit)


for _ in range(1,upper_limit+1):
  