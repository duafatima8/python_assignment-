                                                #   1 personal information
name=str(input("enter your name "))
age=int(input("enter your age "))
city=str(input("enter your city name"))
print(f"hi my name is {name}.I am {age} years old and i live in {city}")


                                                            #  2 age caculator
byear=int(input("enter your birth year "))
cyear=int(input("enter current year "))
realage= cyear - byear
print(f"your age is {realage}")

                                                                #    3 caculator
num1= int(input("enter first number"))
sym=  str(input("enter symbol + - * / % **"))
num2= int( input("enter second number"))
if(sym == "+"):
    print(num1 + num2)

elif(sym == "-"):
    print(num1 - num2)

elif(sym == "*"):
    print(num1 *num2)

elif(sym =="/"):
    print(num1 /num2)

elif(sym =="**"):
    print(num1 **num2)

elif(sym =="%"):
    print(num1 %num2)
else:
    print ("please enter right symbols")

                                                            #  4 rectangular caculator
length=float(input("enter the length of the box/object"))
width=float(input("enter the width of the box/object"))
area=length*width
perimeter = (length + width)*2
print(f"The area of the object is {area}.")
print(f"The perimeter of the object is {perimeter}.")


                                                    #   5  temperature conversion
tcelsius=float(input("Enter the temperature in celsius "))
tfahent=(tcelsius * 9/5) + 32
print(tfahent)

                                                        # 6 positive negative
tnum=complex(input("Enter the number please "))
if(tnum>=0):
    print("this is positive number")
elif(tnum<=0):
  print("this is negative number")
else:
    print("Please enter correct number")


                                                    #   7 Even odd
rnum=int(input("enter the number"))
if(rnum % 2):
  print("This number is odd")
else:
  print("This number is even")
  
                                                #   8 total average marks
eng_marks= float(input("enter you english marks"))
urdu_marks= float(input("enter you urdu marks"))
maths_marks= float(input("enter you maths marks"))
total_marks= eng_marks + urdu_marks + maths_marks
ave_marks = total_marks /2
print(f"your total marks are {total_marks}")
print(f"your average marks are {ave_marks}")


                                                #   9 Shpping Bill
price= float(input("enter price"))
quantity = int(input("enter quantity of the product"))
total=price*quantity
print(f"the total price is {total}, where the quantity are {quantity} and price {price}")

                                                        #   10 voting caculator
theage = int(input("Enter your age please"))
if (theage >= 18):
  print("You're eligible for voting")
elif(theage <18):
      print("You'rnt eligible for voting")
else:
  print("right properly")
                                                        #   11 pass or fail
marks = int(input("Enter your marks please"))
if (marks >= 50):
  print("Congrates!! You're pass")
elif(marks <50):
      print("Oh noo! You're Fail")
else:
  print("right properly")

                                                        # 12  greater or less
numb1= int(input("Enter your firt num "))
numb2= int(input("Enter your sec num "))
if(numb1>numb2):
  print(f"{numb1} is greater,")
elif(numb2>numb1):
    print(f"{numb2} is greater.")
                                                        # 13 password checker
password = str(input("Enter your ppassword "))
if (password == "python123"):
  print("login succesfully")
else:
  print("Incorrect Password")


