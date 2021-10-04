#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

#Welcome
print ("Welcome to Tip 10/12/15/20 Calculator.")

#Total bill
total_bill = float(input("The total bill: $"))

#Tip percentage
percent_tip = float(input("How much tip you want to give? 10/12/15/20? "))
after_percent_tip = 1 + (percent_tip/100)

#Number of people
no_people = int(input("How many people will split for the bill? "))

#Paid bill
total_tip = (total_bill/no_people) * after_percent_tip
result = "{:.2f}".format(round(total_tip, 2))

#Result
print(f"Each person should pay ${result}")

# x = 1
# x += 1
# print (x)
# x += 1
# print (x)

# x += 1
# x -= 1
# x /= 1
# x *= 1