# print("jana")
# print('*' * 10)
import math

# variable
# qty = 1
# qty = 2
# print(qty)

# name = input("what is your name?")
# colour = input("what colour did you like?")
# print (name+ " likes " + colour)

# type conversion
#
# birth_year = input('birthyear')
# print(type(birth_year))
# age = 2024 - int(birth_year)
# print(age)

# weight = int(input('weight:'))
# symbol = input('kg or lbs:')
# if symbol == "kg":
#     converted = weight * 20
#     print ("lbs:" + str(converted))
# else:
#     converted = weight / 10
#     print ("kg:" + str(converted))

# formatted strings
# name = "janarth"
# last = "mohanraj"
# hi = name +' [' + last + ']' +' is a painter'
# hai = f'{name} [{last}] is a painter'
# print(hai)

# string methods
# name = ('janarth')
# print(len(name))
# print(name.upper())
# print(name.find('a'))
# print(name.replace('rth',' mohanraj'))
# print(name.title())
#
# # arithmetic operation
# x = 10
# x *= 10
# print(x)

# operator precedence
# x = 1 + 3 * 10 / 5
# print(x)

# math functions
# x = -1.78272
# print (round(x))
# print(abs(x))
# print(math.floor(2.9))
# print(math.ceil(2.9))

# if statement
# is_hot = True
# is_cold = True
# if is_hot:
#     print("it is hot day")
#     print("drink water")
# if is_cold:
#     print('it is a cold day')
#     print("wear a sweater")
# elif is_cold:
#     print('it is a cold day')
#     print("wear a sweater")
#
# else:
#     print("it is a lovely day")

# house_price = 1000
# buyer = input("buyer:")
# if buyer == "ok":
#     House_price = house_price * 10 / 100
#     print("HOUSE_price:"+ str(House_price))
# else:
#     House_price = house_price * 20 / 100
#     print("HOUSE_price:"+ str(House_price))
#     print("HOUSE_price:",House_price)
#     print(f"HOUSE_price: {House_price}")

# logical operators

# has_good_income = True
# has_good_credit = False
# if has_good_income and not has_good_credit:
#     print("eligible for loan")
# else:
#     print("Not eligible for loan")
# income = input("income:")
# credit = input("credit:")
# if income and credit == "good":
#     print("eligible for loan")
# else:
#     print("not eligible for loan")

# comparision operators

# name = "janarth Mohanraj"
# length = (len(name))
# if length < 3:
#     print ("name atleast be a 3 characters")
# elif length > 50:
#     print( "name can be a maximam of 50 characters")
# else:
#     print("it is a good name")

# weight converter
# weight = int(input("weight: "))
# unit = input("(l)bs or (k)g:")
# if unit.upper() == "L":
#     converted = weight * 2
#     print(f"your weight is {converted} kilos")
#     print("your weight is " + str(converted) + " kilos")
#     print("your weight is",str(converted),"kilos")
# else:
#     print(f'your weight is {weight} pounds')
#     print("your weight is " + str(weight) + " pounds")
#     print("your weight is",str(weight),"pounds")

#
# while loop

# i=1
# while i<=8:
#     print("*" * i)
#     i=i+2
# print("done")
# secret_number = 25
# guess_count = 0
# guess_limit=5
# while guess_count < guess_limit:
#     guess=int(input("guess:"))
#     guess_count = guess_count + 1
#     if guess ==secret_number:
#         print ("stop")
#         break
# else:
#     print("loser")

# condition = ""
# started = False
# while True:
#     condition=input("").lower()
#     if condition == ("start"):
#         if started:
#             print("car is already startd")
#         else:
#             started = True
#             print("start the car")
#     elif condition == ("stop"):
#         if not started:
#             print("car is already stooped")
#         else:
#             started = False
#             print("stop the car")
#     elif condition == ("help"):
#         print("""
# start - start the car
# stop - stop the car
# quit - too quit
#               """)
#     elif condition == ("quit"):
#         break
#     else:
#         print("sorry, we cant help to you")

# for loops
# for item in range(5,10,2):
#     print(item)
# prices =[1,2,2,2,2]
# total = 10
# for price in prices:
#     total= (total + price)
# print("Total: " + str(total))

# nested loops
# for x in range(5):
#     for y in range(4):
#         print(str(x)),( str(y))
#
# for x in range(5):
#     for y in range(4):
#         print(str(x),str(y))
#
# for x in range(5):
#     for y in range(4):
#         print(str(x)+str(y))
#
# for x in range(5):
#     for y in range(4):
#         print(f"({x},{y})")
#
# for x in range(5):
#     for y in range(4):
#         print((x ,y))


# numbers = [1,8,5,3,3]
# for x in numbers:
# #     print("x" * x)
# # inner loop
#     output=""
#     for xx in range(x):
#         output += "x"
#     print(output)





