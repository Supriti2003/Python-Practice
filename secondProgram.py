# string slicing

# a="harry and goblin"
# print(a)
# print(a[0:5])

# a="harry and goblin"
# print(a)
# print(a[:5])

# a="harry and goblin"
# print(a)
# print(a[-4:])

# b="0123456789"
# print(b)
# print(b[::2])

# b="0123456789"
# print(b)
# print(b[:7:2])

# b="0123456789"
# print(b)
# print(b[::-1])

# problem solving

# fibonacci series
# a = 0
# b = 1
#
# n = int(input("Enter a number: "))
#
# if n <= 0:
#     print("Please enter a positive number.")
#
# elif n == 1:
#     print(a)
#
# else:
#     print(a)
#     print(b)
#
#     for i in range(2, n):
#         c = a + b
#         print(c)
#         a = b
#         b = c

#check if numb is prime or not
# num=int(input("Enter a number: "))
# if num<=1:
#     print("this is not a prime number")
# else:
#     for i in range(2,num):
#         if num%i==0:
#             print("this is not a prime number")
#             break
#     else:
#         print("it is a prime number")

# check palindrome or not
# num=int(input("Enter a number: "))
# temp=num
# rev=0
# while num>0:
#     dig=num%10
#     rev=rev*10+dig
#     num=num//10
#
# if rev==temp:
#     print("it is palindrome")
# else:
#     print("it is not palindrome")

# a="OOTD.YOLO.ASAP.BRB.GTG.OTW"
# b=a.split(".")
# print(b)

# sort string alphabetically
# a=input("enter anything here: ")
# b= sorted(a)
# print(b)

# remove given char from string
# a="hello"
# b=a.replace("e","")
# print(b)

# remove dot from the following
# z="F.R.I.E.N.D.S"
# B=z.replace(".","")
# print(B)

# # check number of occurance of substr
# a="she sells seashells on the sea shore"
# b=a.count("sea")
# print("sea is occuring: ",b)

# reverse str
# a=input("enter anything here: ")
# print(a[::-1])

# check if string contains only dig
# a=input("enter anything here: ")
# b=(a.isdigit())
# if b== True:
#     print("contains only digits: ")
# else:
#     print("does not contain digits: ")

# check palindrome
# a=input("enter anything: ")
# rev= a[::-1]
# if a==rev:
#     print("it is palindrome")
# else:
#     print("it is not palindrome")

# find numb of vow of a str
# a=input("enter anything here: ")
# vowels=0
# for i in a:
#     if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
#         vowels+=1
#
# print("no of vow: ",vowels)

# check every word begins with capital letter
# a=input("Enter anything here: ")
# print(a.istitle())




