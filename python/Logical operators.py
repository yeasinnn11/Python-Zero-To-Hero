# logical operators (end,or,not) = used to check if tow or more conditional
#                                  statement's is true

temp = int(input("enter the temperature outside:"))

if temp >= 0 and temp <= 30:
   print("The weather is good today")
   print("Go outside")


elif temp < 0 or temp > 30 :
    print("The weather is sensitive")
    print("Dont go outside")

#if not (temp >= 0 and temp <= 30):
#   print("The weather is good today")
#    print("Go outside")

#elif not (temp < 0 or temp > 30) :
#    print("The weather is sensitive")
#    print("Dont go outside")