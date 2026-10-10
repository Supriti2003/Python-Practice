# print('hello it\'s world')
#this is comment singleline
#creating var
#rule 1
# Name="JHON"
# print(Name)

# even_num=2
# odd_num=3
# sum= even_num+odd_num
# print(sum)

#datatype,userinput
#string input
# name=input("enter your name: ")
# print(name)

#integer input
# age= int(input("enter your age: "))
# print(age)

#float input
# length= float(input("enter length: "))
# print(length)

#eval use
# exp1=eval(input("enter your number: "))
# print(exp1)

#type casting n subtype
# name= "john"
# age=23
# print(type(age))
#implicit--------------------------------------
# a=123
# b=1.23
# print(type(a))
# print(type(b))
# c=a+b
# print(c)
# print(type(c))
#explicit-------------------------------
# a="123"
# b=1.23
# print(type(a))
# print(type(b))
# #conversion
# a=int(a)
# print("after conversion type: ",type(a))
#
# c=a+b
# print(c)
# print(type(c))

#problem set
#print details on 3 diff lines
# name= "ajay"
# age =22
# addr= "delhi"
# print(name)
# print(age)
# print(addr)

# swap two var
# a=12
# b=13
# print("before swap: ",a,b)
# temp=a
# a=b
# b=temp
# print("after swap: ",a,b)

#a,b=b,a
#print(a)
#print(b)

#convert float to int
# x=12.4
# print(type(x))
# x= int(x)
# print(type(x))
# print(x)

#input taking student details
# print("student id card")
# name= input("Enter your name:")
# batch=input("enter your grade: ")
# age= int(input("enter age: "))
#
# print("name: ",name)
# print("batch: ",batch)
# print("age: ",age)

#take int input, convert to float

# x= int(input("enter the number: "))
# print("before conversion: ",x)
# x= float(x)
# print("after conversion: ",x)

#operator and operands
# print(8%3)
# print(8//3)
# print(2**10)

#comparison operator
# print(3<6)
# print(3>6)
# print(3==3)
# print(3!=4)
# print(3>=6)

#logical operators
# print (not(3>4 and 3<4))
# print(3>2 and 3<4)
# print(3>=3 or 4<=3)

#assignment operator
# score=10
# score-=1
# print(score)

# score=10
# score+=1
# print(score)

# score=10
# score*=5
# print(score)

#identity operator
# a=1234
# b="1234"
# print(type(a))
# print(type(b))
#
# print(a is b)

# a=1234
# b="1234"
# print(type(a))
# print(type(b))
#
# print(a is not b)

#bitwise operator
# #binary
# print(bin(15))

#and op
# a=10
# b=8
# print(a & b)

#or op
# a=10
# b=8
# print(a | b)

#xor operator
# a=10
# b=8
# print(a^b)

#zero fill left shift
# print(10>>1)

#zero fill right shift
# print(10<<2)

# membership op
# a= "hello"
# print("e" in a)
#
# a= "hello"
# print("e" not in a)

#conditional op
#if the statement
# marks=100
# if(marks>=90):
#     print('you will get a mobile')
#
# print("thank you")

# else if
#if the statement
# marks=97
# if(marks>=90):
#     print("you win a phn")
# else:
#     print("no phone for 1 month")
#
# print("thank you")

# if elif else
# marks=50
# if marks>=90:
#     print("go to trip")
# elif marks>=80:
#     print("good but no trip")
# elif marks>=70:
#     print("better luck next time")
# else:
#     print("good")
#
# print("thank you")

# method 2
# marks= int(input("enter your marks:"))
# if marks>=90:
#     print("you can go to a trip")
# elif marks>=80 and marks<=90:
#     print("you will get a new phone")
# elif marks>=70 and marks<=80:
#     print("you will get a pen")
# elif marks==50:
#     print("you should improve")
# else:
#     print("thank you for your time")
#
# print("thank you")

# nested if
# marks=75
# if marks>=80:
#     print("you will get new phone")
#     if marks>=95:
#         print("you can go to a new trip")
#
# else:
#     print("no phone for a month")
#
# print("thank you")

# short hand if
# marks=91
# if marks>=90: print("great")
# else: print("not great")

# short hand if-else
# marks=80
# print("a trip for you") if marks>=90 else print("no phone")

# problem solving

#check if number pos or not
# num= int(input("Enter a number: "))
#
# if num>0:
#     print("it is a positive number")
# else:
#     print("it is a negative number")

# check numb is odd or even
# numb=int(input("enter the number: "))
# if numb % 2==0:
#     print("even")
# else:
#     print("odd")

# area calculator
# print("area calculator")
#
# print("""press 1 to get area of square
# press 2 to get the area of rectangle
# press 3 to get the area of circle
# press 4 to get the area of triangle""")
#
# choice=int(input("enter your choice:"))
# if choice==1:
#     side=float(input("enter the length of one side: "))
#     area= side*side
#     print("the area of square is: ",area)
#
# elif choice==2:
#     length=float(input("enter the length of rectangle: "))
#     width=float(input("enter the width of rectangle:"))
#     area= length*width
#     print("the area of rectangle is: ",area)
#
# elif choice==3:
#     radius=float(input("enter the radius of the circle:"))
#     area= (22/7)*(radius**2)
#     print("the area of circle is: ",area)
#
# elif choice==4:
#     base= float(input("enter the base of the triangle: "))
#     height = float(input("enter the height of the triangle: "))
#     area= 0.5*base*height
#     print("the area of triangle is: ",area)
#
# else:
#     print("invalid choice")

#check letter is vowel or not
# letter=input("enter a letter: ")
# if (letter in "aeiou") or (letter in "AEIOU"):
#     print("it is vowel")
# else:
#     print("it is not a vowel")

#check if number ois single digit numb
# num=int(input("ENTER A NUMB: " ))
# if num>=0 and num<=9:
#     print("it is single digit number")
# elif num>=10 and num<=99:
#     print("it is two digit number")
#
# else:
#     print("invalid input")
#
# print("thanks")

#loops
#for loop
# for i in range (1,6):
#     print("hello world")

# for i in range (1,6,2):
#     print("i")

#multiuplication table
# n=int(input("enter number: "))
# for i in range(1,11):
#     print(n,"*",i,"=",n*i)

#while loop
# n=1
# while n<=5:
#     print(n)
#     n=n+2

# table create
# n=1
# a=7
# while n<=10:
#     print(a,"*",n,"=",n*a)
#     n=n+1

# while true
# while True:
#     num1=int(input("enter a number"))
#     num2= int(input(":enter another number"))
#
#     print(num1+num2)
#     repeat=input("do you stop the program?")
#     if repeat=="yes":
#         break

# nested loop
# for i in range(1,4):
#     for j in range(1,11):
#         print(j, end="")
#     print()

# # pattern problem
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j, end= "")
#     print()

# for loop with conditional statement
# for i in range(1,101):
#     if i%8==0 and i%12==0:
#         print(i)

# n=1
# while n<=10:
#     if n==3:
#       print("add this to favs")
#     else:
#       print(n)
#
#     n=n+1

# brEAK AND CONTINUE STATEMENT

# for i in range(1,11):
#     if i==5:
#         continue
#     else:
#         print(i)


# for i in range(1,11):
#     if i==7:
#         break
#     else:
#         print(i)

# problem solving
# sum=0
# for i in range(1,51):
#     if i%2==0:
#         sum=sum+i
#
# print("sum of all even nuber: ",sum)

# for i in range(1,21):
#     print(i,i**2)

# sum of first odd number
# sum=0
# n=0
# while n<=20:
#     if n%2!=0:
#         sum=sum+n
#     n=n+1
# print("sum= ",sum)

# billing system creation
# while True:
#     name= input("Enter customer's name: ")
#     total=0
#
#     while True:
#         print("enter the amount and quantity")
#         amount=int(input("enter the amount: "))
#         quantity=int(input("enter the quantity: "))
#
#         total+=amount*quantity
#         repeat=input("Do you want to continue? (y/n): ")
#         if repeat=="n"or repeat=="N":
#             break
#     print("------")
#     print("name: ",name)
#     print("amount to be paid: ",total)
#     print("------")
#     print("happy shopping")
#
#     repeat1=input("Do you want to continue? (y/n): ")
#     if repeat1=="n"or repeat1=="N":
#         break

# prblm solving

# find lenghth of str
# a="hello"
# b=(len(a))
# print(b)

# how many times alphabet o is occuring
# a="helloo"
# print(a.count("o"))

# convert str into lower n uppercase
# a="Hello"
# b=a.lower()
# print(b)

# a="Hello"
# b=a.upper()
# print(b)

# find index
# a= "Why Fit In, When You Are Born To Stand Out!"
# b=a.find("Fit In")
# print(b)

# string to title
# a= "Why Fit In, When You Are Born To Stand Out!"
# b=a.title()
# print(b)

# pattern prblm
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

# for i in range(1,6):
#     for j in range(6,i,-1):
#         print(j,end=" ")
#     print()

# backward printing
# for i in range(1,6):
#     for j in range(5,i,-1):
#         print(" ",end=" ")
#     for k in range(i):
#         print("*",end=" ")
#     print()

# string manipulation
# a="hello world"
# print(type(a))
# print(len(a))
# print(a.count("o"))
# print(a.upper())
# print (a.lower())
# print(a.index("o"))
# print(a.capitalize())
# print(a.find("l"))

# name="Jhon"
# print(format(name))
# a="my name is",name
# print(a)

# name="jhon"
# print(name.center(10,"*"))

# a="My name is Supriti"
# print(a)
# print(a.casefold())

# name="John"
# age=24
# b="my name is {} and age {}"
# print(b.format(name,age))

# check if alpha numeric or not
# a="hello"
# b="ABC123"
# c='1234'

# print(a,a.isalnum())
# print(b,b.isalnum())
# print(b, b.isalpha())
# print(c, c.isdecimal())
# print (c.isdigit())
# print(c.isnumeric())
# print(a.islower())
# print(a.isupper())

# a="Harry And Goblin"
# print(a.istitle())

# string part 3

# a="harry potter"
# print(a.endswith("r"))

# a="harry potter"
# print(a.endswith("t",6,9))

# a="harry potter"
# print(a.startswith("p",6,9))

# a="Harry potter"
# print(a.swapcase())

# a="  harry**potter"
# print(a.replace("*"," "))

# a="  harry**potter"
# print(a.strip().replace("*"," "))

# a="OOTD#BRB#OMW#TB"
# print(a.split("#"))

# a="hello. my name is supu. i am 23 years old"
# print(a.split("."))

# a="harry potter"
# x=a.ljust(20,"*")
# print(x,"is my fav movie")

# a="harry potter"
# x=a.rjust(20,"*")
# print(x,"is my fav movie")\

# a="my name is supu"
# print(a)
# print(a.replace("supu","tojo"))

# a="harry potter and azkaban"
# print(a.rindex("harry"))

# a="harry potter and the goblet"
# print(a.rfind("potter"))

# a="harry potter"
# print(a.rindex("a",1,4))