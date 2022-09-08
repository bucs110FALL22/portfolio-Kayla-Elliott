print(10*5)
print(10**2) #exponent 
print(15 / 10)
print(15 // 10)
print(-15 // 10) #its rounding down here
print(15%10)
print(10%15)
print(10%10)
print(0%10)
print(10/15) #this repeats the decimal



rate = float(input("What is the current rate from Euro to the American Dollar?:"))
print(rate, "That was the rate you entered")

float(input("Would you like to re-enter the current rate?:"))
#a while loop, won't work otherwise
amount = float(input("Please input the amount to exchange:"))
result = (rate * amount) - 3
print("You have recieved back $", result, "back")

#ask the person to input the amount that the rate is, and asign that to the rate variable, ask the user to input an amount ad save that to Amount

#dont use int when you could use float