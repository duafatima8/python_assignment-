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


                      #  grade calc


tmarks = int(input("Enter your total marks. "))
if(tmarks <=99 and tmarks >= 80):
  print("wow! its an A")
elif(tmarks <=79 and tmarks >= 70):
  print("nice its B")
elif(tmarks <=69 and tmarks >= 60) :
  print("nice its c")
elif(tmarks <=59 and tmarks >= 50):
  print("nice its D")
elif(tmarks <=49 and tmarks >= 0):
  print("oho you are fail")
else:
  print("Please enter right number")

                                          # largest of three
digit1 = int(input("enter any number"))
digit2 = int(input("enter any number  again"))
digit3 = int(input("enter any number again"))
if(digit1 > digit2 and digit1 > digit3):
  print(f"{digit1} is largest")
elif(digit2 > digit1 and digit2 > digit3):
  print(f"{digit2} is largest")
elif(digit3 > digit2 and digit3 > digit1):
  print(f"{digit3} is largest")
else:
  print("error")
                                                  #  17 login checker
user_name =str(input("Enter your user name "))
user_pass =int(input("Enter your user password "))
if (user_name == "admin" and user_pass == 12345):
  print("welocome!")
else:
  print("no no sir this is incorrect")

                                                    #18 if positive so chek even odd
thnum=int(input("Enter the number please "))
if(thnum>=0 and not thnum % 2):
    print("this is positive even number")
if(thnum>=0 and  thnum % 2):
    print("this is positive odd number")

elif(thnum<=0):
  print("this is negative number")
else:
    print("Please enter correct number")

                                                      #19 electricity bill
bill_num = int(input("Enter your electicity bill unit. "))
if(bill_num <=100 ):
 print(bill_num*10)
elif(bill_num >=101 and bill_num <= 200):
 print(bill_num*15)
elif(bill_num >= 201) :
 print(bill_num*20)
else:
  print("Please enter right number")

                                                  #20  CAR checker
cars = ["BMW", "porsche","suzuki", "toyota","Rolls roys"]
yourcar = str(input("Enter what car you want?"))
if (yourcar in cars)
  print("yeah, this car is availaibe")
else:
  print("Sorry,this is'nt available.")


                                            #21  Shpping list checker
cart = ["cheese", "chocolate","milk", "flour","cream"]
youritem = str(input("Enter what item you want?"))
if(youritem in cart ):
  print("yeah you added this")
else:
  print("no sorry")


                                              #22  list to set
numbers = [10, 20, 10, 30, 20, 40, 30]
numbers = set(numbers)
print(numbers)

                                            #23  tuple display
details = ("Ali", "18", "digital marketing", "459")
print(f"My name is {details[0]}. I am {details[1]}years old and I'm doing {details[2]} and i have gain {details[3]} marks ")

                                              #  vowel checker
vowels = ["a" , "e", "i" , "o","u"]
alphabet = str(input("enter any alphabet"))
if(alphabet in vowels):
  print("this is a vowel.")
else:
  print("this is a consonent")

                                                  #  display data type
naam = "duaa"
herage = 16
hermarks = 34.65
theweather = -34
hobbies = ["paint","code","guitar"]
ttb = ("chocolates","coco powder","horlicks","linear brush")
fvtfood = {"ice cream","gol gappay","biryani","chocolate cake","milk cake"}
print(type(naam))
print(type(herage))
print(type(hermarks))
print(type(theweather))
print(type(hobbies))
print(type(ttb))
print(type(fvtfood))

                                          #  converting inputs
numbe1= input("enter any number")
numbe2= input("enter any number again")
numbe1=int(numbe1)
numbe2=int(numbe2)
print(numbe1 + numbe2)



                                    #  converting int but print both
tabs = 34
print(tabs)
print(type(tabs))
tabs = float(tabs)
print(tabs)
print(type(tabs))

                                  # number to string
snum = str(input("enter the number"))
snum= int(snum)
print(f"the answer will be {snum * 10} ")


                          # challenge question
yourname = str(input("enter your name"))
eng_marks = float(input("enter your english number "))
maths_marks = float(input("enter your maths number "))
computer_marks = float(input("enter your computer number "))
ttmarks = eng_marks + maths_marks + computer_marks
average_marks = ttmarks/3
percentage = ttmarks /300 * 100
if(ttmarks >=240 and ttmarks <= 300):
  print(f"wow! your total numbers are {ttmarks} and average number {average_marks} and its an A and the percentage is {percentage}%  ")
elif(ttmarks >=210 and ttmarks <= 239):
    print(f"wow! your total numbers are {ttmarks} and average number {average_marks} and its an B and the percentage is {percentage}%")
elif(ttmarks >=180 and ttmarks <= 209) :
   print(f"oh! your total numbers are {ttmarks} and average number {average_marks} and its an C and the percentage is {percentage}%")
elif(ttmarks >=150 and ttmarks <= 179):
   print(f"hmm your total numbers are {ttmarks} and average number {average_marks} and its an D and the percentage is {percentage}%")
elif(ttmarks >=149 and ttmarks <= 0):
    print(f"tch tch tch! your total numbers are {ttmarks} and average number {average_marks} and its an F and the percentage is {percentage}%")
else:
  print("Please enter right number")




                                        # ATM
acc_balance = float(input("Enter your account balance "))
w_money = float(input("How much money do you want to withdraw"))
if(w_money > acc_balance):
  print("Insufficient Balance")
elif(w_money <= acc_balance):
  print( f" okay this is your remaining amount {acc_balance-w_money}")
else:
  print("no no sorry write right amount ")


                                      #  movie ticket
cage = int(input("enter you age"))
if(cage <=5):
  print("free")
elif(cage >5 and cage <12):
  print("300")
elif(cage >13 and cage <59):
  print("400")
elif(cage >60 ):
  print("600")
else:
  print("enter right number plz")

                                      # student result checker
emarks = float(input("enter your english marks "))
mmarks = float(input("enter your maths marks "))
umarks = float(input("enter your urdu marks "))
if(emarks >=50 and mmarks >=50 and umarks>=50):
  print("yess you are pass")
else:
  print("you're fail")



                                  #discount bill
itemprice = float(input("item price "))
itemquan = int(input("item quantity "))
totalprice = itemprice * itemquan
discount = totalprice * 0.10
if(totalprice >= 5000):
  print(f"{totalprice - discount} is your total price cuz you have got 10% discount")
else:
  print(totalprice)